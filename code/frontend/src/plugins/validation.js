import { extend } from 'vee-validate';
import {
	required,
	email,
	min,
	max,
	confirmed,
	digits,
	min_value,
	max_value,
} from 'vee-validate/dist/rules';

// Defining rules globally
extend('required', {
	...required,
	message: 'This field is required',
});

extend('email', {
	...email,
	message: 'This field should be an email',
});

extend('min', {
	...min,
	message: 'This field is too short',
});

extend('max', {
	...max,
	message: 'This field is too long',
});

extend('confirmed', {
	...confirmed,
	message: 'Password confirmation does not match',
});

// Custom rules
extend('mobile_limit', {
	...digits,
	message: 'This field should be a mobile number',
});

extend('year_limit', {
	...digits,
	message: 'This field should be a year',
});

extend('min_value', {
	...min_value,
	message: 'This field should be above 100',
});

extend('max_value', {
	...max_value,
	message: 'This field should be below 99999999.99',
});
