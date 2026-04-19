<script>

    import { onMount } from "svelte";

    let transactions = $state([]);
    let loading = $state(true);

    async function loadTransactions() {
        const response = await fetch(
            "http://127.0.0.1:8000/transactions"
        );
        transactions = await response.json();
        loading = false;
    }
    onMount(loadTransactions);

</script>

<h1>Transactions</h1>

<table border="1">
    <thead>
        <tr>
            <th>ID</th>
            <th>Description</th>
            <th>Amount</th>
            <th>Date</th>
            <th>Category</th>
        </tr>
    </thead>

    <tbody>
        {#if loading}
            <tr>
                <td colspan="5">Loading data...</td>
            </tr>
        {:else if transactions.length === 0}
            <tr>
                <td colspan="5">No transactions found</td>
            </tr>
        {:else}
            {#each transactions as transaction}
                <tr>
                    <td>{transaction.id}</td>
                    <td>{transaction.description}</td>
                    <td>{transaction.amount}</td>
                    <td>{transaction.date}</td>
                    <td>{transaction.category}</td>
                </tr>
            {/each}
        {/if}
    </tbody>
</table>