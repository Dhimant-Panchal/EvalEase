<script lang="ts">
    import KeywordEntry from "$lib/KeywordEntry.svelte";
    import {
        Button,
        Column,
        Grid,
        Row,
        Tile,
        DataTable,
        NumberInput,
    } from "carbon-components-svelte";
    import type { PageData } from "./$types";
    import { enhance } from "$app/forms";
    import { arraysEqual } from "$lib/ArrayUtils";

    export let data: PageData;
    let interests: string[] = data.profile.interests;
    $: unsaved = !arraysEqual(data.profile.interests, interests);

    const saveKeywords = () => {
        fetch("?/updateinterests", {
            method: "POST",
            body: JSON.stringify({ interests: interests }),
        });
        data.profile.interests = interests;
    };
</script>

<Grid>
    <Row>
        <Column>
            <h1>Academic Home</h1>
            <p style="margin-bottom: var(--cds-layout-03)">
                Use this page to manage your interests and assigned student
                submissions.
            </p>
        </Column>
    </Row>
    <Row>
        <Column>
            <Tile style="margin-bottom: var(--cds-layout-01)">
                <h6 style="margin-bottom: var(--cds-layout-01)">Interests</h6>
                <span
                    style="display:block; margin-bottom: var(--cds-layout-01)"
                >
                    Your interests are used by module conveners to assign you
                    student submissions. The more accurate your keywords are,
                    the more relevant your assigned submissions will be.
                </span>
                <KeywordEntry bind:selection={interests} />
                <Button
                    style="margin-top: var(--cds-layout-01)"
                    type="submit"
                    disabled={!unsaved}
                    on:click={saveKeywords}
                >
                    Apply
                </Button>
            </Tile>
            <form method="post" action="?/submitevaluations" use:enhance>
                <DataTable
                    title="Marking Inbox"
                    description="These submissions have been assigned to you, and are awaiting your mark. Once marked, a submission is hidden."
                    headers={[
                        { key: "assignment_title", value: "Assignment Title" },
                        { key: "module", value: "Module Code" },
                        { key: "urn", value: "Student URN" },
                        { key: "mark", value: "Given Mark" },
                    ]}
                    sortKey="assignment_title"
                    rows={data.inbox}
                >
                    <svelte:fragment slot="cell" let:row let:cell>
                        {#if cell.key === "mark"}
                            <NumberInput
                                light
                                allowEmpty
                                hideSteppers
                                hideLabel
                                size="xl"
                                name={row.id}
                                value={cell.value}
                            ></NumberInput>
                        {:else}
                            {cell.display
                                ? cell.display(cell.value, row)
                                : cell.value}
                        {/if}
                    </svelte:fragment>
                </DataTable>
                <Button type="submit">Submit</Button>
            </form>
        </Column>
    </Row>
</Grid>
