# 注册「每天核对 + 重建 + 部署」的定时任务
#
# 注册（普通 PowerShell 即可，不需要管理员）：
#   powershell -ExecutionPolicy Bypass -File register_daily_task.ps1
#
# 卸载：
#   Unregister-ScheduledTask -TaskName "furadvisor-daily-update" -Confirm:$false
#
# 设计取舍：
#   * 时间定在 09:10，比原来的 GSC 提交任务（09:30）早，这样 GSC 任务跑的时候
#     站点已经是当天核对过的版本。
#   * LogonType Interactive：wrangler 用的是当前用户的 OAuth 令牌，
#     不能在无人登录的会话里跑。机器必须有人登录。
#   * StartWhenAvailable：错过时间（关机）时，开机后补跑一次。
#   * ExecutionTimeLimit 45 分钟：一次完整核对要抓 68 个外部页面，慢但有限。
$ErrorActionPreference = 'Stop'
$taskName = 'furadvisor-daily-update'
$script = Join-Path $PSScriptRoot 'run_daily_update.cmd'

if (-not (Test-Path $script)) { throw "missing $script" }

$action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument "/c `"$script`"" -WorkingDirectory $PSScriptRoot
$trigger = New-ScheduledTaskTrigger -Daily -At '09:10'
$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 45)
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" `
    -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger `
    -Settings $settings -Principal $principal `
    -Description 'Re-verify furadvisor.com facts against the brands'' own pages, rebuild, selfcheck, deploy' `
    -Force | Out-Null

Write-Output "registered: $taskName"
Get-ScheduledTask -TaskName $taskName | Select-Object TaskName, State | Format-Table -AutoSize
(Get-ScheduledTaskInfo -TaskName $taskName) | Select-Object LastRunTime, NextRunTime | Format-Table -AutoSize
