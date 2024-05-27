<script setup>
import router from "../router"
</script>

<template>
	<div class="movie">
		<div class="container">
			<h5>Search for movies based on Movie Name: </h5>
            <br>
			<div>
				<form class="form-inline my-2 my-lg-0" @submit.prevent="searchmovie">
				<input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" v-model="selectedMovie">
				<br>
				<input class="btn btn-outline-success my-2 my-sm-0" type="submit" value="Search">
				</form>
			</div>
			<br>
			<b-table class="border-top" striped :items="items" :fields="fields">
				<template #cell(BookTicket)="row">
					<b-button
						class="button btn btn-yellow"
						size="sm"
						@click="BookTicket(row.item)"
					>
						Book Tickets
					</b-button>
				</template>
			</b-table>
		</div>
	</div>
</template>

<script>

import { mapActions, mapGetters } from 'vuex';

export default {
	name: 'Movie',
	props: ["venue_id"],
	data() {
		return {
			fields: [
				{
					key: 'movie_id',
					label: 'Movie ID',
					class: 'text-center',
				},
				{
					key: 'venue_id',
					label: 'Venue ID',
					class: 'text-center',
				},
				{
					key: 'name',
					label: 'Name',
					class: 'text-center',
				},
				{
					key: 'movie_rating',
					label: 'Movie Rating',
					class: 'text-center',
				},
				{
					key: 'movie_time',
					label: 'Movie Time',
					class: 'text-center',
				},
				{
					key: 'category_name',
					label: 'Category',
					class: 'text-center',
				},
				{
					key: 'ticket_price',
					label: 'Ticket Price',
					class: 'text-center',
				},
				{
					key: 'number_of_seats',
					label: 'Number of Seats',
					class: 'text-center',
				},
				"BookTicket"
			],
			items: [],
			show: false,
			selectedMovie: '',
		};
	},
	methods: {
		...mapActions(['loadMovie', 'loadCategories']),
		...mapGetters(['getMovie', 'getAccessToken', 'getCategories']),
		async searchmovie(){
			await fetch(`http://127.0.0.1:5000/search_movie_keyword/${this.selectedMovie}` , 
			{
				headers: {"Content-Type":"application/json",
				Authorization: `Bearer ${this.getAccessToken()}`}}

			)
			.then(x => x.json())
			.then(data => {
				this.items = data.filter( x => new Date(x.movie_time) >= new Date());
			})
		},
		BookTicket(data){
			router.push(`/useraddbooking/${data.movie_id}`)
		},
		async reloadMovie() {
			await this.loadMovie();
			this.items = (await this.getMovie()).filter(x => parseInt(this.venue_id) == x["venue_id"]);
			this.items = this.items.filter( x => new Date(x.movie_time) >= new Date());
			
		},
	},
	async mounted() {
		await this.reloadMovie();
	},
};
</script>

<style scoped>
.movie {
	padding: 100px 0;
}
.heading {
	font-size: 30px;
	font-weight: 600;
	margin-bottom: 20px;
}
.button {
	margin-right: 10px;
}
.btn-yellow {
	background-color: #e4c314 !important;
	color: #000 !important;
	font-weight: 600;
}
.btn-red {
	background-color: #ff918d;
	color: #000;
	font-weight: 600;
}
.rlink {
	color: #000;
	text-decoration: none;
}
</style>
