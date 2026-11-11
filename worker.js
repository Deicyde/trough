// Answers the requests that name no file of the built site; Cloudflare serves
// every file itself (wrangler.jsonc). "/x/" shows x/index.html, "/x" moves to
// "/x/" when that folder has an index page, and anything else gets the site's
// 404 page.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;
    if (path.endsWith("/")) {
      const index = await env.ASSETS.fetch(new URL(path + "index.html", url));
      if (index.ok) return index;
    } else if (!path.split("/").pop().includes(".")) {
      const index = await env.ASSETS.fetch(new URL(path + "/index.html", url));
      if (index.ok) return Response.redirect(new URL(path + "/" + url.search, url).href, 301);
    }
    const missing = await env.ASSETS.fetch(new URL("/404.html", url));
    return new Response(missing.body, { status: 404, headers: missing.headers });
  },
};
