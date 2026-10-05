// ILANG
// TYPE:worker ROLE:canonical-host-and-real-404
const CANONICAL_HOST = "furadvisor.com";
const VALID_PATHS = new Set(["/", "/0b0ea18577c245daa97fcd9290c9be95.txt", "/about", "/ads.txt", "/assets/appeal-deadlines.svg", "/assets/appeal-flow.svg", "/assets/claim-filing-and-speed.svg", "/assets/claim-windows.svg", "/assets/cost-by-brand.svg", "/assets/favicon.svg", "/assets/lemonade-vs-spot-windows.svg", "/assets/og-best-pet-insurance.png", "/assets/og-exotic-pet-insurance.png", "/assets/og-fetch-pet-insurance.png", "/assets/og-home.png", "/assets/og-how-to-submit-a-pet-insurance-claim.png", "/assets/og-lemonade-cat-insurance.png", "/assets/og-lemonade-pet-insurance.png", "/assets/og-lemonade-vs-spot.png", "/assets/og-pet-insurance-claim-denied.png", "/assets/og-pet-insurance-claim-filing-deadline.png", "/assets/og-pet-insurance-cost-by-brand.png", "/assets/og-pet-insurance-cost.png", "/assets/og-pet-insurance-promo-code.png", "/assets/og-pet-insurance-waiting-periods-by-condition.png", "/assets/og-pet-insurance-waiting-periods.png", "/assets/og-pet-insurance-wellness-add-on.png", "/assets/og-spot-pet-insurance.png", "/assets/promo-discounts.svg", "/assets/published-prices.svg", "/assets/state-averages.svg", "/assets/style.css", "/assets/waiting-period-day-counts.svg", "/assets/waiting-periods.svg", "/assets/wellness-schedules.svg", "/best-pet-insurance", "/contact", "/exotic-pet-insurance", "/fetch-pet-insurance", "/how-to-submit-a-pet-insurance-claim", "/lemonade-cat-insurance", "/lemonade-pet-insurance", "/lemonade-vs-spot", "/llms-full.txt", "/llms.txt", "/pet-insurance-claim-denied", "/pet-insurance-claim-filing-deadline", "/pet-insurance-cost", "/pet-insurance-cost-by-brand", "/pet-insurance-promo-code", "/pet-insurance-waiting-periods", "/pet-insurance-waiting-periods-by-condition", "/pet-insurance-wellness-add-on", "/privacy", "/robots.txt", "/sitemap.xml", "/spot-pet-insurance"]);

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.hostname !== CANONICAL_HOST) {
      return Response.redirect(new URL(url.pathname + url.search, `https://${CANONICAL_HOST}`).toString(), 301);
    }

    const path = url.pathname.replace(/\/+$/, "") || "/";

    if (path.endsWith(".html")) {
      const bare = path === "/index.html" ? "/" : path.slice(0, -5);
      if (VALID_PATHS.has(bare)) {
        return Response.redirect(new URL(bare + url.search, `https://${CANONICAL_HOST}`).toString(), 308);
      }
    }

    if (VALID_PATHS.has(path)) {
      return env.ASSETS.fetch(request);
    }

    const notFound = await env.ASSETS.fetch(new URL("/404.html", url));
    return new Response(notFound.body, {
      status: 404,
      headers: {
        "content-type": "text/html; charset=utf-8",
        "cache-control": "no-store",
        "x-robots-tag": "noindex",
      },
    });
  },
};
