<script lang="ts">
    import {
        Search,
        Tag,
        ListBoxMenu,
        ListBoxMenuItem,
    } from "carbon-components-svelte";
    import { onMount } from "svelte";
    import Checkmark from "carbon-icons-svelte/lib/Checkmark.svelte";
    import KeywordList from "./KeywordList.svelte";

    export let selection: string[] = [];

    let value: string;
    let options: string[];
    $: if (!value || value.length == 0) options = [];

    let showOptions = false;
    let selectedIndex = 0;
    $: selectedIndex =
        options.length > 0 ? Math.min(selectedIndex, options.length - 1) : 0;

    onMount(() => {
        let lastQuery = value;
        const handle = setInterval(() => {
            if (value === undefined || value.length == 0) {
                options = [];
            } else if (lastQuery != value) {
                fetch(`/api/keyword/search/${value}/`).then(async (p) => {
                    if (p.ok) options = await p.json();
                });
            }
            lastQuery = value;
        }, 200);
        return () => clearInterval(handle);
    });

    const onSelect = (index: number) => {
        const item = options[index];
        if (selection.includes(item)) {
            selection = selection.filter((o) => o != item);
        } else {
            selection = [...selection, item];
        }
    };
</script>

<KeywordList filter bind:selection />

<div role="listbox" style="position: relative;">
    <Search
        light
        on:clear={() => (options = [])}
        on:focus={() => (showOptions = true)}
        on:blur={(e) => {
            // 'Blur' swallows outside clicking.
            // Propagate the click event to choose a ListBoxMenuItem, before we hide it.
            e.relatedTarget?.dispatchEvent(new Event("click"));
            showOptions = false;
        }}
        on:keydown={(e) => {
            const { key } = e;

            if (options.length == 0) return;

            let delta = 0;
            if (key === "ArrowDown") {
                delta = 1;
                e.preventDefault();
            } else if (key === "ArrowUp") {
                delta = -1;
                e.preventDefault();
            } else if (key === "Tab") {
                delta = 1;
                e.preventDefault();
            } else if (key === "Enter") {
                onSelect(selectedIndex);
                e.preventDefault();
            }

            selectedIndex =
                (options.length + selectedIndex + delta) % options.length;
        }}
        bind:value
    />
    {#if showOptions}
        <ListBoxMenu>
            {#each options as opt, i}
                <ListBoxMenuItem
                    highlighted={selectedIndex == i}
                    on:click={() => onSelect(i)}
                >
                    {opt}
                    {#if selection.includes(opt)}
                        <Checkmark style="position:absolute; right: 20;" />
                    {/if}
                </ListBoxMenuItem>
            {/each}
        </ListBoxMenu>
    {/if}
</div>
