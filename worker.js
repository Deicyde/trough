// Answers the requests that name no file of the built site; Cloudflare serves
// every file itself (wrangler.jsonc). "/x/" shows x/index.html. "/x" moves to
// "/x/" when that folder has an index page, or else to "/x.html" when that file
// exists, as GitHub Pages served it. Anything else gets the site's 404 page.
// Every address is set on a copy of the request's URL, with repeated slashes
// merged first, so no request can send a reader to another host.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const at = (pathname) => {
      const target = new URL(url);
      target.pathname = pathname;
      return target;
    };
    const path = url.pathname.replace(/\/{2,}/g, "/");
    if (path !== url.pathname) return Response.redirect(at(path).href, 301);
    if (path.endsWith("/")) {
      const index = await env.ASSETS.fetch(at(path + "index.html"));
      if (index.ok) return index;
    } else if (!path.split("/").pop().includes(".")) {
      for (const [file, address] of [[path + "/index.html", path + "/"], [path + ".html", path + ".html"]]) {
        if ((await env.ASSETS.fetch(at(file))).ok) return Response.redirect(at(address).href, 301);
      }
    }
    const missing = await env.ASSETS.fetch(at("/404.html"));
    return new Response(missing.body, { status: 404, headers: missing.headers });
  },
};
