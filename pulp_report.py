import pandas as pd

def save_results_to_dataframe(dataframe, model_name, scenario):
	
	# Activate variable names in "var_dict" to be included in the results,
	# or comment out all redundant variables.
	
	df = dataframe
	
	var_dict = {

		########			Demands 					#############
		#"RateOfDemand": ["r", "l", "f", "y"],
		"Demand": ["r", "l", "f", "y"],

		########     		Storage                 		#############
		#"RateOfStorageCharge": ["r", "s", "ls", "ld", "lh", "y"],
		#"RateOfStorageDischarge": ["r", "s", "ls", "ld", "lh", "y"],
		#"NetChargeWithinYear": ["r", "s", "ls", "ld", "lh", "y"],
		#"NetChargeWithinDay": ["r", "s", "ls", "ld", "lh", "y"],
		#"StorageLevelYearStart": ["r", "s", "y"],
		#"StorageLevelYearFinish": ["r", "s", "y"],
		#"StorageLevelSeasonStart": ["r", "s", "ls", "y"],
		#"StorageLevelDayTypeStart": ["r", "s", "ls", "ld", "y"],
		#"StorageLevelDayTypeFinish": ["r", "s", "ls", "ld", "y"],
		#"StorageLowerLimit": ["r", "s", "y"],
		#"StorageUpperLimit": ["r", "s", "y"],
		#"AccumulatedNewStorageCapacity": ["r", "s", "y"],
		#"NewStorageCapacity": ["r", "s", "y"],
		#"CapitalInvestmentStorage": ["r", "s", "y"],
		#"DiscountedCapitalInvestmentStorage": ["r", "s", "y"],
		#"SalvageValueStorage": ["r", "s", "y"],
		#"DiscountedSalvageValueStorage": ["r", "s", "y"],
		#"TotalDiscountedStorageCost": ["r", "s", "y"],

		#########		    Capacity Variables 			#############
		#"NumberOfNewTechnologyUnits": ["r", "t", "y"],
		"NewCapacity": ["r", "t", "y"],
		#"AccumulatedNewCapacity": ["r", "t", "y"],
		"TotalCapacityAnnual": ["r", "t", "y"],

		#########		    Activity Variables 			#############
		#"RateOfActivity": ["r", "l", "t", "m", "y"],
		#"RateOfTotalActivity": ["r", "t", "l", "y"],
		#"TotalTechnologyAnnualActivity": ["r", "t", "y"],
		#"TotalAnnualTechnologyActivityByMode": ["r", "t", "m", "y"],
		#"TotalTechnologyModelPeriodActivity": ["r", "t"],
		#"RateOfProductionByTechnologyByMode": ["r", "l", "t", "m", "f", "y"],
		#"RateOfProductionByTechnology": ["r", "l", "t", "f", "y"],
		#"ProductionByTechnology": ["r", "l", "t", "f", "y"],
		#"ProductionByTechnologyAnnual": ["r", "t", "f", "y"],
		#"RateOfProduction": ["r", "l", "f", "y"],
		#"Production": ["r", "l", "f", "y"],
		#"RateOfUseByTechnologyByMode": ["r", "l", "t", "m", "f", "y"],
		#"RateOfUseByTechnology": ["r", "l", "t", "f", "y"],
		#"UseByTechnologyAnnual": ["r", "t", "f", "y"],
		#"RateOfUse": ["r", "l", "f", "y"],
		#"UseByTechnology": ["r", "l", "t", "f", "y"],
		#"Use": ["r", "l", "f", "y"],
		#"Trade": ["r", "rr", "l", "f", "y"],
		#"TradeAnnual": ["r", "rr", "f", "y"],
		#"ProductionAnnual": ["r", "f", "y"],
		"UseAnnual": ["r", "f", "y"],

		#########		    Costing Variables 			#############
		"CapitalInvestment": ["r", "t", "y"],
		#"DiscountedCapitalInvestment": ["r", "t", "y"],
		#"SalvageValue": ["r", "t", "y"],
		#"DiscountedSalvageValue": ["r", "t", "y"],
		#"OperatingCost": ["r", "t", "y"],
		#"DiscountedOperatingCost": ["r", "t", "y"],
		#"AnnualVariableOperatingCost": ["r", "t", "y"],
		#"AnnualFixedOperatingCost": ["r", "t", "y"],
		"TotalDiscountedCostByTechnology": ["r", "t", "y"],
		#"TotalDiscountedCost": ["r", "y"],
		#"ModelPeriodCostByRegion": ["r"],

		#########			Reserve Margin				#############
		#"TotalCapacityInReserveMargin": ["r", "y"],
		#"DemandNeedingReserveMargin": ["r", "l", "y"],

		#########			RE Gen Target				#############
		#"TotalREProductionAnnual": ["r", "y"],
		#"RETotalProductionOfTargetFuelAnnual": ["r", "y"],

		#########			Emissions					#############
		#"AnnualTechnologyEmissionByMode": ["r", "t", "e", "m", "y"],
		#"AnnualTechnologyEmission": ["r", "t", "e", "y"],
		#"AnnualTechnologyEmissionPenaltyByEmission": ["r", "t", "e", "y"],
		#"AnnualTechnologyEmissionsPenalty": ["r", "t", "y"],
		#"DiscountedTechnologyEmissionsPenalty": ["r", "t", "y"],
		"AnnualEmissions": ["r", "e", "y"],
		"ModelPeriodEmissions": ["r", "e"]
	}

	# Objective value ("cost")
	df_temp = pd.DataFrame(columns=[
		'SCENARIO',
		'VAR_NAME',
		'VAR_VALUE',
		'REGION',
		'REGION2',
		'DAYTYPE',
		'EMISSION',
		'FUEL',
		'DAILYTIMEBRACKET',
		'SEASON',
		'TIMESLICE',
		'MODE_OF_OPERATION',
		'STORAGE',
		'TECHNOLOGY',
		'YEAR',
		'FLEXIBLEDEMANDTYPE'])

	df_temp.at[0, 'SCENARIO'] = scenario
	df_temp.at[0, 'VAR_NAME'] = "cost"
        #df_temp.at[0, 'VAR_VALUE'] = model_name.objective.value()
	df_temp.at[0, 'REGION'] = " "
	df_temp.at[0, 'REGION2'] = " "
	df_temp.at[0, 'DAYTYPE'] = " "
	df_temp.at[0, 'EMISSION'] = " "
	df_temp.at[0, 'FUEL'] = " "
	df_temp.at[0, 'DAILYTIMEBRACKET'] = " "
	df_temp.at[0, 'SEASON'] = " "
	df_temp.at[0, 'TIMESLICE'] = " "
	df_temp.at[0, 'MODE_OF_OPERATION'] = " "
	df_temp.at[0, 'STORAGE'] = " "
	df_temp.at[0, 'TECHNOLOGY'] = " "
	df_temp.at[0, 'YEAR'] = " "
	df_temp.at[0, 'FLEXIBLEDEMANDTYPE'] = " "

	df = pd.concat([df, df_temp])

	# Variables values (only variables that are included in var_dict)
	selected_variables = [variable for key in var_dict.keys() for variable in model_name.component_objects(ctype=Var) if key == variable.name.split("_")[0]]

	for var in selected_variables:

		# Temporal dataframe in loop
		df_temp = pd.DataFrame(columns=[
			'SCENARIO',
			'VAR_NAME',
			'VAR_VALUE',
			'REGION',
			'REGION2',
			'DAYTYPE',
			'EMISSION',
			'FUEL',
			'DAILYTIMEBRACKET',
			'SEASON',
			'TIMESLICE',
			'MODE_OF_OPERATION',
			'STORAGE',
			'TECHNOLOGY',
			'YEAR',
			'FLEXIBLEDEMANDTYPE'])

		# Variable name
		var_name = var.name.split("_")[0]

		# Variable indices
		var_concrete_indices_list = var.name.split("_")[1:]

		# Variable abstract indices
		var_abstract_indices_list = var_dict[var_name]

		# Dictionary
		abstract_dict = {key: "" for key in ["r", "rr", "ld", "e", "f", "lh", "ls", "l", "m", "s", "t", "y", "fdt"]}  # default value: " "
		concrete_dict = {key: value for key, value in zip(var_abstract_indices_list, var_concrete_indices_list)}
		data_dict = {**abstract_dict, **concrete_dict}  # Merge dictionaries

		# Write data to dataframe
		df_temp.at[0, 'SCENARIO'] = scenario
		df_temp.at[0, 'VAR_NAME'] = var.name.split("_")[0]
		df_temp.at[0, 'VAR_VALUE'] = var.varValue
		df_temp.at[0, 'REGION'] = data_dict["r"]
		df_temp.at[0, 'REGION2'] = data_dict["rr"]
		df_temp.at[0, 'DAYTYPE'] = data_dict["ld"]
		df_temp.at[0, 'EMISSION'] = data_dict["e"]
		df_temp.at[0, 'FUEL'] = data_dict["f"]
		df_temp.at[0, 'DAILYTIMEBRACKET'] = data_dict["lh"]
		df_temp.at[0, 'SEASON'] = data_dict["ls"]
		df_temp.at[0, 'TIMESLICE'] = data_dict["l"]
		df_temp.at[0, 'MODE_OF_OPERATION'] = data_dict["m"]
		df_temp.at[0, 'STORAGE'] = data_dict["s"]
		df_temp.at[0, 'TECHNOLOGY'] = data_dict["t"]
		df_temp.at[0, 'YEAR'] = data_dict["y"]
		df_temp.at[0, 'FLEXIBLEDEMANDTYPE'] = data_dict["fdt"]

		df = pd.concat([df, df_temp])

	return df


def save_results(dataframe, file_path):
	df = dataframe
	name_list = df['VAR_NAME'].unique()
	dataframe_list = [df[df['VAR_NAME'] == str(name)] for name in name_list]
	writer = pd.ExcelWriter(file_path)

	for df, name in zip(dataframe_list, name_list):
		df.to_excel(writer, sheet_name=name, index=False)
	writer.save()
	return