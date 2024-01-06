<script>
    import { Alert } from 'flowbite-svelte';
    export let events;
    let counter = 0;
    let incCounter = () => counter++;
    import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
</script>
  <Table striped={true}>
    <TableHead>
      <TableHeadCell>Product name</TableHeadCell>
      <TableHeadCell>Color</TableHeadCell>
      <TableHeadCell>Category</TableHeadCell>
      <TableHeadCell>Price</TableHeadCell>
      <TableHeadCell>
        <span class="sr-only">Edit</span>
      </TableHeadCell>
    </TableHead>
    <TableBody class="divide-y">
    {#each events as event}
      <TableBodyRow>
        <TableBodyCell>{event.name}</TableBodyCell>
        <TableBodyCell>Sliver</TableBodyCell>
        <TableBodyCell>Laptop</TableBodyCell>
        <TableBodyCell>$2999</TableBodyCell>
        <TableBodyCell>
          <a href="/tables" class="font-medium text-primary-600 hover:underline dark:text-primary-500">Edit</a>
        </TableBodyCell>
      </TableBodyRow>
    {/each}
    </TableBody>
  </Table>