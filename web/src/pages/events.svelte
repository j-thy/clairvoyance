<script>
  import { Alert } from 'flowbite-svelte';
  export let events;
  let counter = 0;
  let incCounter = () => counter++;
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
  import { Img } from 'flowbite-svelte';
</script>
  <Table striped={true}>
    <TableHead>
      <TableHeadCell>Image</TableHeadCell>
      <TableHeadCell>Event</TableHeadCell>
      <TableHeadCell>Region</TableHeadCell>
    </TableHead>
    <TableBody class="divide-y">
    {#each events as event}
      <TableBodyRow>
        <TableBodyCell><Img src="/static/event_imgs/{event.image_file}" alt="sample 1" size="h-16" class="rounded-lg" /></TableBodyCell>
        <TableBodyCell>{event.name}</TableBodyCell>
        <TableBodyCell>{event.region}</TableBodyCell>
      </TableBodyRow>
    {/each}
    </TableBody>
  </Table>