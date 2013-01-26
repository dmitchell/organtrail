var MechanicsModel = Backbone.Model.extend({
	defaults: {
		id: null,
		name: "Checkup",
		description: "Go see your doctor.",
		timeCost: 1,
		moneyCost: 100,
		successRate: 0.1,
		donorPoolImpact: 0.1,
		recipientListImpact: 0.1,
	}
});

var Mechanics = Backbone.Collection.extend({
	url : "mechanic",
	model : MechanicsModel
});

// populates the table
var MechanicsCollectionView = Backbone.View.extend({
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