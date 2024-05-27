<template>
	<div class="customer">
		<div class="container">
			<div class="heading">Customers</div>
			<b-table
				class="border-top"
				striped
				:items="items"
				:fields="fields"
			></b-table>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
	name: 'Customer',
	data() {
		return {
			fields: [
				{
					key: 'cust_id',
					label: 'Customer ID',
					class: 'text-center',
				},
				{
					key: 'name',
					label: 'Name',
				},
				{
					key: 'email',
					label: 'Email',
				},
				{
					key: 'phone',
					label: 'Phone',
				},
				{
					key: 'address',
					label: 'Address',
					thStyle: 'width: 30%;',
				},
			],
			items: [],
		};
	},
	methods: {
		...mapGetters(['getAccessToken']),
		async loadAdminCustomers() {
			await axios
				.get('http://localhost:5000/admincustomers', {
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${this.getAccessToken()}`
					},
				})

				.then((response) => {
					this.items = response.data;
					this.items.forEach(x=>{x["phone"] = parseInt(x["phone"])})
				});
		},
	},
	mounted() {
		this.loadAdminCustomers();
	},
};
</script>

<style scoped>
.customer {
	padding: 100px 0;
}
.heading {
	font-size: 30px;
	font-weight: 600;
	margin-bottom: 50px;
}
</style>
