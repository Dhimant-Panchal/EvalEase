<script lang="ts">
    import {
        Column,
        DataTable,
        Grid,
        Link,
        Row,
    } from "carbon-components-svelte";
    import type { PageData } from "./$types";
    import { page } from "$app/stores";
    import { formatDateTime } from "$lib/DateUtils";

    export let data: PageData;
</script>

<Grid>
    <Row>
        <Column>
            <h1>Module</h1>
            <p style="margin-bottom: var(--cds-layout-03)">
                Edit and view module information.
            </p>
        </Column>
    </Row>
    <Row>
        <Column>
            <DataTable
                title="Assignments"
                description="Manage your submissions for assignments associated with this module."
                headers={[
                    { key: "title", value: "Name" },
                    { key: "due_date", value: "Due Date" },
                ]}
                sortKey="due_date"
                rows={data.assignments}
            >
                <svelte:fragment slot="cell" let:row let:cell>
                    {#if cell.key === "title"}
                        <Link href="../assignments/{row.id}/">{cell.value}</Link
                        >
                    {:else if cell.value instanceof Date}
                        {formatDateTime(cell.value)}
                    {:else}
                        {cell.value}
                    {/if}
                </svelte:fragment>
            </DataTable>
        </Column>
    </Row>
</Grid>
