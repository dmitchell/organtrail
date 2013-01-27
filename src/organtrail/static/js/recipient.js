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
	model : RecipientModel,
	updateState : function(partialModels) {
		_.each(partialModels, function(update) {
			this.get(update.id).set(update);
		}, this);
	}
});

// populates the table
var RecipientCollectionView = Backbone.View.extend({
	initialize: function() {
		this.template = _.template('<tr class="patient-row">' +
				'<td class="patient-pos"><%= model.get("rank") %></td>' +
				'<td class="patient-name"><%= model.get("name") %></td>' +
				'<td class="patient-ttl"><%= model.get("lifeExpectancy") %>d</td></tr>');
		this.listenTo(this.collection, 'change', this.render);
		this.listenTo(this.collection, 'reset', this.render);
	},
	updatePlayer : function() {
		var player = window.recipients.get(window.currentPlayer);
		if (player.has("doctor")) {
			var doctor = window.doctors.get(player.get("doctor"));
			$("#player-doctor").html(doctor.get("name"));
		}
		$("#player-money").html("$" + player.get("money"));
	},
	render : function() {
		this.$el.html('');
		var sortedCollection = this.collection.sortBy(function(ele) { return -ele.get("rank"); });
		for (var i = 0; i < this.collection.length; i++) {
			this.$el.append(this.template({model : sortedCollection[i]}));
		}
		// update current user's cash
		this.updatePlayer();
	}
});

