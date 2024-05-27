<template>
	<div class="movie">
		<div class="container">
			<div class="heading">Movies</div>
			<button class="btn btn-yellow" style="marginbottom: 20px">
				<router-link class="rlink" :to="`/adminaddmovie/${venue_id}`">
					+ Add Movie
				</router-link>
			</button>
			<b-table class="border-top" striped :items="items" :fields="fields">
				<template #cell(update)="row">
					<b-button
						class="button btn btn-yellow"
						size="sm"
						@click="routeUpdateMovie(row.item)"
					>
						Modify
					</b-button>
				</template>
				<template #cell(delete)="row">
					<b-button
						class="btn btn-red"
						size="sm"
						@click="showDeletionModal(row.item.movie_id)"
					>
						Delete
					</b-button>
				</template>
			</b-table>
			<b-modal
				v-model="show"
				id="delete-movie"
				title="Confirm movie deletion"
			>
				<p class="my-4">Are your sure you want to delete this movie?</p>
				<template #modal-footer>
					<b-button
						size="md"
						class="float-right btn btn-red"
						@click="show = false"
					>
						Cancel
					</b-button>
					<b-button
						size="md"
						class="float-right btn btn-yellow"
						@click="deleteMovie()"
					>
						Delete Movie
					</b-button>
				</template>
			</b-modal>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
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
					key: 'category_id',
					label: 'Category ID',
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
				"update","delete"
			],
			items: [],
			show: false,
			selectedMovie: '',
		};
	},
	created(){
		console.log(this.venue_id)	
	},
	methods: {
		...mapActions(['loadMovie', 'routeModifyMovie']),
		...mapGetters(['getMovie', 'getAccessToken']),
		showDeletionModal(movie_id) {
			this.show = true;

			this.selectedMovie = movie_id;
		},
		routeUpdateMovie(movieData) {
			this.routeModifyMovie(movieData);
			this.$router.push(`/adminmodifymovie/${movieData.movie_id}`);
		},
		async deleteMovie() {
			await axios
				.delete(`http://localhost:5000/deletemovie/${this.selectedMovie}`, {
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${this.getAccessToken()}`
					},
				})
				.then(() => {
					alert('Movie deleted successfully!');
				})
				.catch(() => {
					alert('Error deleting movie!');
				});
			this.show = false;
			await this.reloadMovie();
		},
		async reloadMovie() {
			await this.loadMovie();
			this.items = (await this.getMovie()).filter(x => x.venue_id==this.venue_id);
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
