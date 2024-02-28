   
from django.db import models

class Beneficiation(models.Model):
    # Date and hour fields
    date = models.DateField()
    hour = models.PositiveSmallIntegerField()

    # Throughput fields
    rom_feed_to_plant_dry_ta = models.PositiveIntegerField()
    feed_to_leach_dry_ta = models.PositiveIntegerField()
    ctfs_total_tailing_dry_ta = models.PositiveIntegerField()
    lce_produced_dry_ta = models.PositiveIntegerField()

    # Crushing fields
    rom_li_content_ppm = models.PositiveIntegerField()
    particle_size_distribution_f80_mm = models.PositiveIntegerField()
    ore_bulk_density_transport_tm3 = models.FloatField()
    ore_moisture_total_loose_weight_percent = models.FloatField()
    crushed_particle_size_p80_mm = models.PositiveIntegerField()
    feed_to_attrition_circuit_dry_td = models.PositiveIntegerField()
    discharge_screen_oversize_rom_percent = models.FloatField()

    # Classification fields
    feed_particle_size_p80_microns = models.PositiveIntegerField()
    overflow_particle_size_p80_microns = models.PositiveIntegerField()
    underflow_particle_size_p80_microns = models.PositiveIntegerField()
    coarse_material_rejection_dry_percent = models.FloatField()
    thickener_underflow_pulp_density_weight_percent = models.FloatField()
    flocculant_consumption_g_per_t = models.FloatField()
    decanter_centrifuge_cake_density_weight_percent = models.FloatField()

    # Leach fields
    feed_solids_li_content_ppm = models.PositiveIntegerField()
    feed_pulp_density_weight_percent = models.FloatField()
    leach_residence_time_minutes = models.PositiveIntegerField()

    # Neutralization fields
    neutralization_tank_limestone_residence_time_minutes = models.PositiveIntegerField()
    neutralization_tank_mgoh2_residence_time_minutes = models.PositiveIntegerField()
    ph_in_final_neutralization_tank = models.FloatField()
    neutralization_clarifier_flocculant_consumption_g_per_t = models.FloatField()

    # CCD and Filtration fields
    no_of_ccd_stages = models.PositiveIntegerField()
    ccd_filtration_recovery_percent = models.FloatField()
    flocculant_consumption_total_g_per_t = models.FloatField()
    filtration_residual_moisture_in_cake_percent = models.FloatField()

    def __str__(self):
        return f"{self.date} {self.hour}: Beneficiation KPIs"
    class Meta:
        pass  # Empty Meta class

class Mines(models.Model):
    From_MineTPH = models.PositiveIntegerField()
    ScrubberTPH = models.PositiveIntegerField()
    ThickenerTPH = models.PositiveIntegerField()
    CoarseGangueM3PH = models.PositiveIntegerField()
    RecycleWaterM3PH = models.PositiveIntegerField()
    Notes = models.CharField(max_length=200)

    def __Int__(self): 
        return self.From_MineTPH
    class Meta:
        pass  # Empty Meta class    


class DieselFleet(models.Model):
    oil_changes = models.PositiveIntegerField(default=1)
    battery_change = models.PositiveIntegerField(default=3)

    class Meta:
        pass  # Empty Meta class


class ProcessPlant(models.Model):
    mg_sulfate_stages_evaporation = models.PositiveIntegerField(default=1)
    mg_sulfate_stages_crystallization = models.PositiveIntegerField(default=3)
    mg_removal_percentage = models.PositiveIntegerField(default=79)
    centrifuge_cake_moisture_mg = models.PositiveIntegerField(default=4)

    residual_magnesium_content_ppm = models.PositiveIntegerField(default=5)
    mg_oh2_recycle_stream_pulp_density = models.PositiveIntegerField(default=30)

    residual_calcium_content_ppm = models.PositiveIntegerField(default=100)
    underflow_solids_density_calcium = models.PositiveIntegerField(default=5)

    residual_calcium_content_ion_exchange = models.CharField(max_length=20, default="Proprietary")
    residual_magnesium_content_ion_exchange = models.CharField(max_length=20, default="Proprietary")
    residual_boron_content_ion_exchange = models.CharField(max_length=20, default="Proprietary")

    lithium_carbonate_stages_crystallization = models.PositiveIntegerField(default=2)
    lithium_carbonate_stages_bicarbonation = models.PositiveIntegerField(default=1)
    second_stage_centrifuge_cake_moisture = models.PositiveIntegerField(default=20)
    zld_centrifuge_cake_moisture = models.PositiveIntegerField(default=15)
    dryer_discharge_moisture = models.FloatField(default=0.1)
    jet_mill_discharge_particle_size = models.PositiveIntegerField(default=6)
    cooler_discharge_temperature = models.PositiveIntegerField(default=40)

    notes = models.CharField(max_length=200, default="")

    def __int__(self): 
        return self.mg_sulfate_stages_evaporation  # Return any field you wish as default
    class Meta:
        pass  # Empty Meta class
