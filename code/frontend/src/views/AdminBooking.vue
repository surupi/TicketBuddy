<template>
	<div class="customer">
		<div class="container">
			<div class="heading">Bookings</div>
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
					key: 'booking_id',
					label: 'Booking ID',
					class: 'text-center',
				},
				{
					key: 'cust_id',
					label: 'Customer ID',
				},
                {
					key: 'venue_id',
					label: 'Venue ID',
				},
				{
					key: 'movie_id',
					label: 'Movie ID',
				},
				{
					key: 'number_of_tickets',
					label: 'Number of Tickets',
				},
			],
			items: [],
		};
	},
	methods: {
		...mapGetters(['getAccessToken']),
		async loadAdminBooking() {
			await axios
				.get('http://localhost:5000/adminbooking', {
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
		this.loadAdminBooking();
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