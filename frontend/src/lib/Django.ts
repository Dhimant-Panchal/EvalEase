import type { Cookies } from "@sveltejs/kit";

export function getDjHeaders(cookies: Cookies) {
    return {
        "Authorization": `Token ${cookies.get("token")}`,
        'Content-Type': 'application/json',
    }
}