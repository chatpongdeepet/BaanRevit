__title__ = "Imperial"
__author__ = "Chatpong Deepet"
__doc__ = """Convert project unit to imperial unit (inch)"""

#
# * Created by SharpDevelop.
# * User: CHATPONG
# * Date: 28/08/2566
# * Time: 21:46
# *
# * To change this template use Tools | Options | Coding | Edit Standard Headers.
#
from System import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from System.Collections.Generic import *

if __name__ == '__main__':
    doc = __revit__.ActiveUIDocument.Document
    uidoc = __revit__.ActiveUIDocument

    rounding = 0.01

    units = doc.GetUnits()
    # Length
    length = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_IN, rounding)
    units.SetFormatOptions(UnitType.UT_Length, length)
    # AREA
    area = FormatOptions(DisplayUnitType.DUT_SQUARE_INCHES, UnitSymbolType.UST_IN_SUP_2, rounding)
    units.SetFormatOptions(UnitType.UT_Area, area)
    # VOLUME
    volume = FormatOptions(DisplayUnitType.DUT_CUBIC_FEET, UnitSymbolType.UST_FT_SUP_3, rounding)
    units.SetFormatOptions(UnitType.UT_Volume, volume)
    # ANGLE
    angle = FormatOptions(DisplayUnitType.DUT_DECIMAL_DEGREES, UnitSymbolType.UST_DEGREE_SYMBOL, rounding)
    units.SetFormatOptions(UnitType.UT_Angle, angle)
    # Slope
    slope = FormatOptions(DisplayUnitType.DUT_1_RATIO, UnitSymbolType.UST_ONE_COLON, rounding)
    units.SetFormatOptions(UnitType.UT_Slope, slope)
    # MASS DENSITY
    massDensity = FormatOptions(DisplayUnitType.DUT_POUNDS_MASS_PER_CUBIC_FOOT, UnitSymbolType.UST_LB_MASS_PER_CU_FT,
                                rounding)
    units.SetFormatOptions(UnitType.UT_MassDensity, massDensity)
    # FORCE
    force = FormatOptions(DisplayUnitType.DUT_KIPS, UnitSymbolType.UST_KIP, rounding)
    units.SetFormatOptions(UnitType.UT_Force, force)
    # LINEAR FORCE
    linear_force = FormatOptions(DisplayUnitType.DUT_KIPS_PER_FOOT, UnitSymbolType.UST_KIP_PER_FT, rounding)
    units.SetFormatOptions(UnitType.UT_LinearForce, linear_force)
    # AREA FORCE
    area_force = FormatOptions(DisplayUnitType.DUT_KIPS_PER_SQUARE_FOOT, UnitSymbolType.UST_KIP_PER_SQ_FT, rounding)
    units.SetFormatOptions(UnitType.UT_AreaForce, area_force)
    # MOMENT
    moment = FormatOptions(DisplayUnitType.DUT_KIP_FEET, UnitSymbolType.UST_KIP_DASH_FT, rounding)
    units.SetFormatOptions(UnitType.UT_Moment, moment)
    # UNIT WEIGHT
    unit_weight = FormatOptions(DisplayUnitType.DUT_KIPS_PER_CUBIC_INCH, UnitSymbolType.UST_KIP_PER_IN_SUP_3, rounding)
    units.SetFormatOptions(UnitType.UT_UnitWeight, unit_weight)
    # WEIGHT
    weight = FormatOptions(DisplayUnitType.DUT_POUNDS_FORCE, UnitSymbolType.UST_LB_FORCE, rounding)
    units.SetFormatOptions(UnitType.UT_Weight, weight)
    # MASS
    mass = FormatOptions(DisplayUnitType.DUT_POUNDS_MASS, UnitSymbolType.UST_LB_MASS,rounding)
    units.SetFormatOptions(UnitType.UT_Mass, mass)
    # MASS PER UNIT AREA
    mass_per_unit_area = FormatOptions(DisplayUnitType.DUT_POUNDS_MASS_PER_SQUARE_FOOT,
                                       UnitSymbolType.UST_LBM_PER_SQ_FT, rounding)
    units.SetFormatOptions(UnitType.UT_MassPerUnitArea, mass_per_unit_area)
    # THERMAL EXPANSION COEFFICIENT
    therm_ex_coef = FormatOptions(DisplayUnitType.DUT_INV_FAHRENHEIT, UnitSymbolType.UST_INV_DEGREE_F, rounding)
    units.SetFormatOptions(UnitType.UT_ThermalExpansion, therm_ex_coef)
    # DISPLACEMENT-DEFLECTION
    displacement_deflection = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_IN, rounding)
    units.SetFormatOptions(UnitType.UT_Displacement_Deflection, displacement_deflection)
    # ROTATION
    rotation = FormatOptions(DisplayUnitType.DUT_RADIANS, UnitSymbolType.UST_RAD, rounding)
    units.SetFormatOptions(UnitType.UT_Rotation, rotation)
    # PERIOD
    period = FormatOptions(DisplayUnitType.DUT_SECONDS, UnitSymbolType.UST_S, rounding)
    units.SetFormatOptions(UnitType.UT_Period, period)
    # VELOCITY
    velocity = FormatOptions(DisplayUnitType.DUT_FEET_PER_SECOND, UnitSymbolType.UST_FT_PER_S, rounding)
    units.SetFormatOptions(UnitType.UT_Structural_Velocity, velocity)
    # ACCELERATION
    acceleration = FormatOptions(DisplayUnitType.DUT_FEET_PER_SECOND_SQUARED, UnitSymbolType.UST_FT_PER_SQ_S, rounding)
    units.SetFormatOptions(UnitType.UT_Acceleration, acceleration)
    # REINFORCEMENT VOLUME
    reinforcement_volume = FormatOptions(DisplayUnitType.DUT_CUBIC_INCHES, UnitSymbolType.UST_IN_SUP_3, rounding)
    units.SetFormatOptions(UnitType.UT_Reinforcement_Volume, reinforcement_volume)
    # REINFORCEMENT LENGTH
    reinforcement_length = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_INCH_DOUBLE_QUOTE, rounding)
    units.SetFormatOptions(UnitType.UT_Reinforcement_Length, reinforcement_length)
    # REINFORCEMENT AREA
    reinforcement_area = FormatOptions(DisplayUnitType.DUT_SQUARE_INCHES, UnitSymbolType.UST_IN_SUP_2, rounding)
    units.SetFormatOptions(UnitType.UT_Reinforcement_Area, reinforcement_area)
    # REINFORCEMENT AREA PER UNIT
    reinforcement_area_per_unit = FormatOptions(DisplayUnitType.DUT_SQUARE_INCHES_PER_FOOT, UnitSymbolType.UST_SQ_IN_PER_FT, rounding)
    units.SetFormatOptions(UnitType.UT_Reinforcement_Area_per_Unit_Length, reinforcement_area_per_unit)
    # REINFORCEMENT SPACING
    reinforcement_spacing = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_INCH_DOUBLE_QUOTE, rounding)
    units.SetFormatOptions(UnitType.UT_Reinforcement_Spacing, reinforcement_spacing)
    # REINFORCEMENT COVER
    reinforcement_cover = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_IN, rounding)
    units.SetFormatOptions(UnitType.UT_Reinforcement_Cover, reinforcement_cover)
    # Bar Diameter
    bar_diameter = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_IN, rounding)
    units.SetFormatOptions(UnitType.UT_Bar_Diameter, bar_diameter)
    # CRACK WIDTH
    crack_width = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_IN, rounding)
    units.SetFormatOptions(UnitType.UT_Crack_Width, crack_width)
    # SECTION DIMENSION
    section_dimension = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_IN, rounding)
    units.SetFormatOptions(UnitType.UT_Section_Dimension, section_dimension)
    # SECTION PROPERTY
    section_property = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_IN, rounding)
    units.SetFormatOptions(UnitType.UT_Section_Property, section_property)
    # SECTION AREA
    section_area = FormatOptions(DisplayUnitType.DUT_SQUARE_INCHES, UnitSymbolType.UST_IN_SUP_2, rounding)
    units.SetFormatOptions(UnitType.UT_Section_Area, section_area)
    # SECTION MODULUS
    section_modulus = FormatOptions(DisplayUnitType.DUT_CUBIC_INCHES, UnitSymbolType.UST_IN_SUP_3, rounding)
    units.SetFormatOptions(UnitType.UT_Section_Modulus, section_modulus)
    # MOMENT OF INERTIA
    moment_of_inertia = FormatOptions(DisplayUnitType.DUT_INCHES_TO_THE_FOURTH_POWER, UnitSymbolType.UST_IN_SUP_4, rounding)
    units.SetFormatOptions(UnitType.UT_Moment_of_Inertia, moment_of_inertia)
    # WARPING CONSTANT
    warpping_constant = FormatOptions(DisplayUnitType.DUT_INCHES_TO_THE_SIXTH_POWER, UnitSymbolType.UST_IN_SUP_6, rounding)
    units.SetFormatOptions(UnitType.UT_Warping_Constant, warpping_constant)
    # MASS PER UNIT LENGTH
    mass_per_length = FormatOptions(DisplayUnitType.DUT_POUNDS_MASS_PER_FOOT, UnitSymbolType.UST_LB_MASS_PER_FT, rounding)
    units.SetFormatOptions(UnitType.UT_Mass_per_Unit_Length, mass_per_length)
    # WEIGHT PER UNIT LENGTH
    weight_per_length = FormatOptions(DisplayUnitType.DUT_POUNDS_FORCE_PER_FOOT, UnitSymbolType.UST_LB_FORCE_PER_FT, rounding)
    units.SetFormatOptions(UnitType.UT_Weight_per_Unit_Length, weight_per_length)
    # SURFACE AREA PER UNIT LENGTH
    surface_area_per_length = FormatOptions(DisplayUnitType.DUT_SQUARE_FEET_PER_FOOT, UnitSymbolType.UST_SQ_FT_PER_FT, rounding)
    units.SetFormatOptions(UnitType.UT_Surface_Area, surface_area_per_length)
    # DENSITY
    density = FormatOptions(DisplayUnitType.DUT_POUNDS_MASS_PER_CUBIC_FOOT, UnitSymbolType.UST_LB_MASS_PER_CU_FT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Density, density)
    # FRICTION
    friction = FormatOptions(DisplayUnitType.DUT_INCHES_OF_WATER_PER_100FT, UnitSymbolType.UST_IN_WG_PER_100FT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Friction, friction)
    # POWER
    power = FormatOptions(DisplayUnitType.DUT_WATTS, UnitSymbolType.UST_WATT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Power, power)
    # POWER DENSITY
    power_density = FormatOptions(DisplayUnitType.DUT_WATTS_PER_SQUARE_FOOT, UnitSymbolType.UST_WATT_PER_SQ_FT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Power_Density, power_density)
    # PRESSURE
    pressure = FormatOptions(DisplayUnitType.DUT_POUNDS_FORCE_PER_SQUARE_INCH, UnitSymbolType.UST_PSI, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Pressure, pressure)
    # TEMPERATURE
    temperature = FormatOptions(DisplayUnitType.DUT_KELVIN, UnitSymbolType.UST_KELVIN, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Temperature, temperature)
    # VELOCITY
    velocity = FormatOptions(DisplayUnitType.DUT_FEET_PER_MINUTE, UnitSymbolType.UST_FT_PER_MIN, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Velocity, velocity)
    # AIR FLOW
    air_flow = FormatOptions(DisplayUnitType.DUT_CUBIC_FEET_PER_MINUTE, UnitSymbolType.UST_CFM, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Airflow, air_flow)
    # DUCT SIZE
    duct_size = FormatOptions(DisplayUnitType.DUT_FEET_FRACTIONAL_INCHES, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_DuctSize, duct_size)
    # CROSS SECTION
    cross_section = FormatOptions(DisplayUnitType.DUT_SQUARE_FEET, UnitSymbolType.UST_FT_SUP_2, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_CrossSection, cross_section)
    # HEAT GAIN
    heat_gain = FormatOptions(DisplayUnitType.DUT_WATTS, UnitSymbolType.UST_WATT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_HeatGain, heat_gain)
    # ROUGHNESS
    roughness = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_IN, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Roughness, roughness)
    # DYNAMIC VISCOSITY
    dynamic_Viscosity = FormatOptions(DisplayUnitType.DUT_POUNDS_MASS_PER_FOOT_SECOND, UnitSymbolType.UST_LBM_PER_FT_S, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Viscosity, dynamic_Viscosity)
    # AIR FLOW DENSITY
    air_flow_density = FormatOptions(DisplayUnitType.DUT_CUBIC_FEET_PER_MINUTE_SQUARE_FOOT, UnitSymbolType.UST_CFM_PER_SQ_FT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Airflow_Density, air_flow_density)
    # COOLING LOAD
    cooling_load = FormatOptions(DisplayUnitType.DUT_WATTS, UnitSymbolType.UST_WATT, 1)
    units.SetFormatOptions(UnitType.UT_HVAC_Cooling_Load, cooling_load)
    # HEATING LOAD
    heating_load = FormatOptions(DisplayUnitType.DUT_WATTS, UnitSymbolType.UST_WATT, 1)
    units.SetFormatOptions(UnitType.UT_HVAC_Heating_Load, heating_load)
    # COOLING LOAD DIVIDED BY AREA
    cooling_load_div_area = FormatOptions(DisplayUnitType.DUT_WATTS_PER_SQUARE_FOOT, UnitSymbolType.UST_WATT_PER_SQ_FT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Cooling_Load_Divided_By_Area, cooling_load_div_area)
    # HEATING LOAD DIVIDED BY AREA
    heating_load_div_area = FormatOptions(DisplayUnitType.DUT_WATTS_PER_SQUARE_FOOT, UnitSymbolType.UST_WATT_PER_SQ_FT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Heating_Load_Divided_By_Area, heating_load_div_area)
    # COOLING LOAD DIVIDED BY VOLUME
    cooling_load_div_volume = FormatOptions(DisplayUnitType.DUT_WATTS_PER_CUBIC_FOOT, UnitSymbolType.UST_WATT_PER_CU_FT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Cooling_Load_Divided_By_Volume, cooling_load_div_volume)
    # HEATING LOAD DIVIDED BY VOLUME
    heating_load_div_volume = FormatOptions(DisplayUnitType.DUT_WATTS_PER_CUBIC_FOOT, UnitSymbolType.UST_WATT_PER_CU_FT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Heating_Load_Divided_By_Volume, heating_load_div_volume)
    # AIR FLOW DIVIDED BY VOLUME
    air_flow_div_volume = FormatOptions(DisplayUnitType.DUT_CUBIC_FEET_PER_MINUTE_CUBIC_FOOT, UnitSymbolType.UST_CFM_PER_CU_FT, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Airflow_Divided_By_Volume, air_flow_div_volume)
    # AIR FLOW DIVIDED BY COOLING LOAD
    air_flow_div_cooling_load = FormatOptions(DisplayUnitType.DUT_CUBIC_FEET_PER_MINUTE_TON_OF_REFRIGERATION, UnitSymbolType.UST_CFM_PER_TON, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Airflow_Divided_By_Cooling_Load, air_flow_div_cooling_load)
    # AREA DIVIDED BY COOLING LOAD
    area_div_cooling_load = FormatOptions(DisplayUnitType.DUT_SQUARE_FEET_PER_TON_OF_REFRIGERATION, UnitSymbolType.UST_SQ_FT_PER_TON, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Area_Divided_By_Cooling_Load, area_div_cooling_load)
    # AREA DIVIDED BY HEATING LOAD
    area_div_heating_load = FormatOptions(DisplayUnitType.DUT_SQUARE_FEET_PER_THOUSAND_BRITISH_THERMAL_UNITS_PER_HOUR, UnitSymbolType.UST_SQ_FT_PER_MBH, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Area_Divided_By_Heating_Load, area_div_heating_load)
    # DUCT INSULATION THICKNESS
    duct_insulation_thickness = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_INCH_DOUBLE_QUOTE, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_DuctInsulationThickness, duct_insulation_thickness)
    # DUCT LINING THICKNESS
    duct_lining_thickness = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_INCH_DOUBLE_QUOTE, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_DuctLiningThickness, duct_lining_thickness)
    # CURRENT
    current = FormatOptions(DisplayUnitType.DUT_AMPERES, UnitSymbolType.UST_AMPERE, rounding)
    units.SetFormatOptions(UnitType.UT_Electrical_Current, current)
    # ELECTRICAL POTENTIAL
    electrical_potential = FormatOptions(DisplayUnitType.DUT_VOLTS, UnitSymbolType.UST_VOLT, 1)
    units.SetFormatOptions(UnitType.UT_Electrical_Potential, electrical_potential)
    # FREQUENCY
    frequency = FormatOptions(DisplayUnitType.DUT_HERTZ, UnitSymbolType.UST_HZ, 1)
    units.SetFormatOptions(UnitType.UT_Electrical_Frequency, frequency)
    # ILLUMINANCE
    illuminance = FormatOptions(DisplayUnitType.DUT_FOOTCANDLES, UnitSymbolType.UST_FC, 1)
    units.SetFormatOptions(UnitType.UT_Electrical_Illuminance, illuminance)
    # LUMINOUS FLUX
    luminous_flux = FormatOptions(DisplayUnitType.DUT_LUMENS, UnitSymbolType.UST_LM, 1)
    units.SetFormatOptions(UnitType.UT_Electrical_Luminous_Flux, luminous_flux)
    # LUMINOUS INTENSITY
    luminous_intensity = FormatOptions(DisplayUnitType.DUT_CANDELAS, UnitSymbolType.UST_CD, 1)
    units.SetFormatOptions(UnitType.UT_Electrical_Luminous_Intensity, luminous_intensity)
    # EFFICACY
    efficacy = FormatOptions(DisplayUnitType.DUT_LUMENS_PER_WATT, UnitSymbolType.UST_LM_PER_W, rounding)
    units.SetFormatOptions(UnitType.UT_Electrical_Efficacy, efficacy)
    # WATTAGE
    wattage = FormatOptions(DisplayUnitType.DUT_WATTS, UnitSymbolType.UST_WATT, rounding)
    units.SetFormatOptions(UnitType.UT_Electrical_Wattage, wattage)
    # COLOR TEMPERATURE
    color_temperature = FormatOptions(DisplayUnitType.DUT_KELVIN, UnitSymbolType.UST_KELVIN, 1)
    units.SetFormatOptions(UnitType.UT_Color_Temperature, color_temperature)
    # POWER
    power = FormatOptions(DisplayUnitType.DUT_WATTS, UnitSymbolType.UST_WATT, 1)
    units.SetFormatOptions(UnitType.UT_Electrical_Power, power)
    # APPARENT POWER
    apparent_power = FormatOptions(DisplayUnitType.DUT_VOLT_AMPERES, UnitSymbolType.UST_VOLTAMPERE, 1)
    units.SetFormatOptions(UnitType.UT_Electrical_Apparent_Power, apparent_power)
    # POWER DENSITY
    power_density = FormatOptions(DisplayUnitType.DUT_WATTS_PER_SQUARE_FOOT, UnitSymbolType.UST_WATT_PER_SQ_FT, 1)
    units.SetFormatOptions(UnitType.UT_Electrical_Power_Density, power_density)
    # ELECTRICAL RESISTIVITY
    electrical_resistivity = FormatOptions(DisplayUnitType.DUT_OHM_METERS, UnitSymbolType.UST_OHM_M, rounding)
    units.SetFormatOptions(UnitType.UT_Electrical_Resistivity, electrical_resistivity)
    # WIRE DIAMETER
    wire_diameter = FormatOptions(DisplayUnitType.DUT_FRACTIONAL_INCHES)
    units.SetFormatOptions(UnitType.UT_WireSize, wire_diameter)
    # TEMPERATURE
    temperature = FormatOptions(DisplayUnitType.DUT_KELVIN, UnitSymbolType.UST_KELVIN, rounding)
    units.SetFormatOptions(UnitType.UT_Electrical_Temperature, temperature)
    # CABLE TRAY SIZE
    cable_tray_size = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_INCH_DOUBLE_QUOTE, rounding)
    units.SetFormatOptions(UnitType.UT_Electrical_CableTraySize, cable_tray_size)
    # CONDUIT SIZE
    conduit_size = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_INCH_DOUBLE_QUOTE, rounding)
    units.SetFormatOptions(UnitType.UT_Electrical_ConduitSize, conduit_size)
    # DENSITY
    density = FormatOptions(DisplayUnitType.DUT_POUNDS_MASS_PER_CUBIC_FOOT, UnitSymbolType.UST_LB_MASS_PER_CU_FT, rounding)
    units.SetFormatOptions(UnitType.UT_Piping_Density, density)
    # FLOW
    flow = FormatOptions(DisplayUnitType.DUT_LITERS_PER_MINUTE, UnitSymbolType.UST_L_PER_M, rounding)
    units.SetFormatOptions(UnitType.UT_Piping_Flow, flow)
    # FRICTION
    friction = FormatOptions(DisplayUnitType.DUT_FEET_OF_WATER_PER_100FT, UnitSymbolType.UST_FT_OF_WATER_PER_100FT, rounding)
    units.SetFormatOptions(UnitType.UT_Piping_Friction, friction)
    # PRESSURE
    pressure = FormatOptions(DisplayUnitType.DUT_POUNDS_FORCE_PER_SQUARE_INCH, UnitSymbolType.UST_PSI, rounding)
    units.SetFormatOptions(UnitType.UT_Piping_Pressure, pressure)
    # TEMPERATURE
    pipe_temperature = FormatOptions(DisplayUnitType.DUT_KELVIN, UnitSymbolType.UST_KELVIN, 0.1)
    units.SetFormatOptions(UnitType.UT_Piping_Temperature, pipe_temperature)
    # VELOCITY
    velocity = FormatOptions(DisplayUnitType.DUT_FEET_PER_SECOND, UnitSymbolType.UST_FT_PER_S, rounding)
    units.SetFormatOptions(UnitType.UT_Piping_Velocity, velocity)
    # DYNAMIC VISCOSITY
    pipe_dynamic_viscosity = FormatOptions(DisplayUnitType.DUT_POUNDS_MASS_PER_FOOT_HOUR, UnitSymbolType.UST_LBM_PER_FT_H, rounding)
    units.SetFormatOptions(UnitType.UT_Piping_Viscosity, pipe_dynamic_viscosity)
    # PIPE SIZE
    pipe_size = FormatOptions(DisplayUnitType.DUT_FRACTIONAL_INCHES)
    units.SetFormatOptions(UnitType.UT_PipeSize, pipe_size)
    # ROUGHNESS
    pipe_roughness = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_INCH_DOUBLE_QUOTE, rounding)
    units.SetFormatOptions(UnitType.UT_Piping_Roughness, pipe_roughness)
    # VOLUME
    pipe_volume = FormatOptions(DisplayUnitType.DUT_CUBIC_FEET, UnitSymbolType.UST_FT_SUP_3, rounding)
    units.SetFormatOptions(UnitType.UT_Piping_Volume, pipe_volume)
    # PIPE INSULATION THICKNESS
    pipe_insulation_thickness = FormatOptions(DisplayUnitType.DUT_DECIMAL_INCHES, UnitSymbolType.UST_INCH_DOUBLE_QUOTE, rounding)
    units.SetFormatOptions(UnitType.UT_PipeInsulationThickness, pipe_insulation_thickness)
    # PIPE DIMENSION
    pipe_dimension = FormatOptions(DisplayUnitType.DUT_FRACTIONAL_INCHES, 0.1)
    units.SetFormatOptions(UnitType.UT_Pipe_Dimension, pipe_dimension)
    # MASS
    pipe_mass = FormatOptions(DisplayUnitType.DUT_POUNDS_MASS, UnitSymbolType.UST_LB_MASS, rounding)
    units.SetFormatOptions(UnitType.UT_PipeMass, pipe_mass)
    # MASS PER UNIT LENGTH
    pipe_mass_per_length = FormatOptions(DisplayUnitType.DUT_POUNDS_MASS_PER_FOOT, UnitSymbolType.UST_LB_MASS_PER_FT, rounding)
    units.SetFormatOptions(UnitType.UT_PipeMassPerUnitLength, pipe_mass_per_length)
    # ENERGY
    energy = FormatOptions(DisplayUnitType.DUT_KILOWATT_HOURS, UnitSymbolType.UST_KWH, 0.1)
    units.SetFormatOptions(UnitType.UT_HVAC_Energy, energy)
    # COEFFICIENT OF HEAT TRANSFER
    coefficient_of_heat_transfer = FormatOptions(DisplayUnitType.DUT_BRITISH_THERMAL_UNITS_PER_HOUR_SQUARE_FOOT_FAHRENHEIT, UnitSymbolType.UST_BTU_PER_H_SQ_FT_DEGREE_F, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_CoefficientOfHeatTransfer, coefficient_of_heat_transfer)
    # THERMAL RESISTANCE
    thermal_resistance = FormatOptions(DisplayUnitType.DUT_HOUR_SQUARE_FOOT_FAHRENHEIT_PER_BRITISH_THERMAL_UNIT, UnitSymbolType.UST_H_SQ_FT_DEGREE_F_PER_BTU, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_ThermalResistance, thermal_resistance)
    # THERMAL MASS
    thermal_mass = FormatOptions(DisplayUnitType.DUT_BRITISH_THERMAL_UNIT_PER_FAHRENHEIT, UnitSymbolType.UST_BTU_PER_F, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_ThermalMass, thermal_mass)
    # THERMAL CONDUCTIVITY
    thermal_conductivity = FormatOptions(DisplayUnitType.DUT_BRITISH_THERMAL_UNITS_PER_HOUR_FOOT_FAHRENHEIT, UnitSymbolType.UST_BTU_PER_H_FT_DEGREE_F, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_ThermalConductivity, thermal_conductivity)
    # SPECIFIC HEAT
    specific_heat = FormatOptions(DisplayUnitType.DUT_BRITISH_THERMAL_UNITS_PER_POUND_FAHRENHEIT, UnitSymbolType.UST_BTU_PER_LB_DEGREE_F, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_SpecificHeat, specific_heat)
    # SPECIFIC HEAT OF VAPORIZATION
    specific_heat_of_vaporization = FormatOptions(DisplayUnitType.DUT_BRITISH_THERMAL_UNITS_PER_POUND, UnitSymbolType.UST_BTU_PER_LB, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_SpecificHeatOfVaporization, specific_heat_of_vaporization)
    # PERMEABILITY
    permeability = FormatOptions(DisplayUnitType.DUT_GRAINS_PER_HOUR_SQUARE_FOOT_INCH_MERCURY, UnitSymbolType.UST_GR_PER_H_SQ_FT_IN_HG, rounding)
    units.SetFormatOptions(UnitType.UT_HVAC_Permeability, permeability)

    transaction = Transaction(doc)
    transaction.Start("Convert Unit")
    doc.SetUnits(units)

    transaction.Commit()
