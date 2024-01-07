<script>
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
  import { Img } from 'flowbite-svelte';
  import { ListPlaceholder } from 'flowbite-svelte';
  import { router } from '@inertiajs/svelte'
	import { onMount } from 'svelte';
  export let events = undefined;
  import { inertia, Link } from '@inertiajs/svelte'

  // mounted() in VueJS / useEffect() in React
  onMount(() => {
    // We fire a partial reload to load the data in:
    router.reload({ only: ['events'] })
  })
</script>
  <Table striped={true}>
    <a href="/events?page=2" use:inertia="{{ only: ['events'] }}">Show active</a>
    <TableHead>
      <TableHeadCell>Image</TableHeadCell>
      <TableHeadCell>Event</TableHeadCell>
      <TableHeadCell>Region</TableHeadCell>
    </TableHead>
    {#if events === undefined}
      <ListPlaceholder />
    {:else}
      <TableBody class="divide-y">
    {#each events as event}
      <TableBodyRow>
        <TableBodyCell><Img src="/static/event_imgs/{event.image_file}" alt="sample 1" size="h-16" class="rounded-lg" /></TableBodyCell>
        <TableBodyCell>{event.name}</TableBodyCell>
        <TableBodyCell>{event.region}</TableBodyCell>
      </TableBodyRow>
    {/each}
    </TableBody>
    {/if}
  </Table>