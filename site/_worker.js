// ILANG
// TYPE:worker ROLE:canonical-host-and-real-404
const CANONICAL_HOST = "furadvisor.com";
const VALID_PATHS = new Set(["/", "/about", "/assets/appeal-deadlines.svg", "/assets/appeal-flow.svg", "/assets/claim-filing-and-speed.svg", "/assets/claim-windows.svg", "/assets/cost-by-brand.svg", "/assets/favicon.svg", "/assets/lemonade-vs-spot-windows.svg", "/assets/promo-discounts.svg", "/assets/published-prices.svg", "/assets/state-averages.svg", "/assets/style.css", "/assets/waiting-period-day-counts.svg", "/assets/waiting-periods.svg", "/assets/wellness-schedules.svg", "/best-pet-insurance", "/contact", "/fetch-pet-insurance", "/how-to-submit-a-pet-insurance-claim", "/lemonade-pet-insurance", "/lemonade-vs-spot", "/pet-insurance-claim-denied", "/pet-insurance-claim-filing-deadline", "/pet-insurance-cost", "/pet-insurance-cost-by-brand", "/pet-insurance-promo-code", "/pet-insurance-waiting-periods", "/pet-insurance-waiting-periods-by-condition", "/pet-insurance-wellness-add-on", "/privacy", "/robots.txt", "/sitemap.xml", "/spot-pet-insurance"]);

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
