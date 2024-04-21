export function formatDateTime(obj: Date | string): string {
    const date = obj instanceof Date ? obj : new Date(obj);
    return date.toLocaleDateString() + ", " + date.toLocaleTimeString([], {
        hourCycle: "h12",
        hour: "numeric",
        minute: "2-digit"
    })
}