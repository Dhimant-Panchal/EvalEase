import { getDjHeaders } from "$lib/Django";
import type { ServerLoad } from "@sveltejs/kit";

export const load: ServerLoad = async ({ fetch, setHeaders, request, cookies }) => {
    // https://web.dev/articles/user-preference-media-features-headers.
    if (!request.headers.get("Accept-CH"))
        setHeaders({
            "Accept-CH": "Sec-CH-Prefers-Color-Scheme",
            "Vary": "Sec-CH-Prefers-Color-Scheme",
            "Critical-CH": "Sec-CH-Prefers-Color-Scheme"
        })

    const res = await fetch("/api/cworker/me/name", { method: "GET", headers: getDjHeaders(cookies) });

    return {
        name: res.ok ? await res.json() : undefined
    }
};