var DoctorModel = Backbone.Model.extend({
	defaults: {
		id: null,
		name: "John Doe",
		waitTime: 30, // days to be seen by doctor
		description: "A long string to show as description--narrative.",
		rating: 78, // quality of care, i.e. likeliness he'll bump you up the list
		cost: 0.2, // money cost of seeing doctor
	}
});

var Doctors = Backbone.Collection.extend({
	url : "doctors",
	model : DoctorModel
});

// populates the table
var DoctorCollectionView = Backbone.View.extend({
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