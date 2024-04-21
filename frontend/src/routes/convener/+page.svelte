<script lang="ts">
    import {
        Button,
        Column,
        Grid,
        Row,
        Tile,
        DataTable,
        Link,
    } from "carbon-components-svelte";
    import type { PageData } from "./$types";
    import { formatDateTime } from "$lib/DateUtils";

    export let data: PageData;
</script>

<Grid>
    <Row>
        <Column>
            <h1>Convener Home</h1>
            <p style="margin-bottom: var(--cds-layout-03)">
                Use this page to manage your assigned modules' assignments.
            </p>
        </Column>
    </Row>
    <Row>
        <Column>
            <DataTable
                title="Assignments"
                description="These assignments are convened by you."
                headers={[
                    { key: "title", value: "Title" },
                    { key: "module", value: "Module Code" },
                    { key: "user_count", value: "Student Count" },
                    { key: "due_date", value: "Due", display: formatDateTime },
                ]}
                sortKey="module"
                rows={data.assignments}
            >
                <svelte:fragment slot="cell" let:row let:cell>
                    {#if cell.key === "title"}
                        <Link href="convener/assignment/{row.id}"
                            >{cell.value}</Link
                        >
                    {:else}
                        {cell.display
                            ? cell.display(cell.value, row)
                            : cell.value}
                    {/if}
                </svelte:fragment>
            </DataTable>
        </Column>
    </Row>
</Grid>
