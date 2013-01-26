var RecipientModel = Backbone.Model.extend({
	defaults: {
		id: null,
		name: "John Doe",
		lifeExpectancy: 30, // days which the client will change as part of count down and actions
		description: "A long string to show as description--narrative.",
		age: 78,
		rejectionProbability: 0.2, // base probability which the client will change based on actions
		doctor: null // the id of the doctor
	}
});

var Recipients = Backbone.Collection.extend({
	url : "recipient",
	model : RecipientModel
});

// populates the table
var RecipientCollectionView = Backbone.View.extend({
	initialize: function() {
		this.template = _.template('<tr class="patient-row">' +
				'<td class="patient-pos"><%= index + 1 %></td>' +
				'<td class="patient-name"><%= model.get("name") %></td>' +
				'<td class="patient-ttl"><%= model.get("lifeExpectancy") %>d</td></tr>');
	},
	render : function() {
		this.$el.html('');
		for (var i = 0; i < this.collection.length; i++) {
			this.$el.append(this.template({index : i, model : this.collection.at(i)}));
		}
	}
})