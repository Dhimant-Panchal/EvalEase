import type { Handle } from '@sveltejs/kit';
export const handle: Handle = async ({ event, resolve }) => {
    const use_dark = event.request.headers.get("sec-ch-prefers-color-scheme") == "dark"
    const response = await resolve(event, {
        transformPageChunk: ({ html }) => html.replace('<html', `<html theme='${use_dark ? "g90" : "g10"}' `)
    });
    return response;
};