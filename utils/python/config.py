# Basic Configuration
# ===================

# Chip - Uncomment one of the lines below
# ---------------------------------------

# chip = 'bcm4339'    # Nexus 5
chip = 'bcm43455c0' # Raspberry Pi 3B+ and 4B
# chip = 'bcm4358'    # Nexus 6P
# chip = 'bcm4366c0'  # Asus RT-AC86U


# Fileroot - Path to the directory with .pcap files
# -------------------------------------------------

pcap_fileroot = 'pcapfiles'


# Miscellaneous
# -------------

print_samples = True  # Set this to False to stop printing to terminal
plot_samples = True   # Set this to False to stop plotting
plot_animation_delay_s = 0.005 # Delay between csi plots.

remove_null_subcarriers = True
remove_pilot_subcarriers = False




# Advanced configuration. You don't need to change this
# =====================================================

# Decoder
# -------

if chip in ['bcm4339', 'bcm43455c0']:
    decoder = 'interleaved'
elif chip in ['bcm4358', 'bcm4366c0']:
    decoder = 'floatingpoint'
else:
    decoder = chip


help_str = f'''
CSI Reader
==========

A simple Python utility to
explore nexmon_csi CSI samples.

Change the config.py to match your
WiFi chip and bandwidth. Current chip
is {chip}.

To explore a sample, type it's
index from the pcap file. Indexes
start from 0.

To plot a range of samples as animation,
type their indexes separated by '-'.

Type 'help' to see this message again.

Type 'exit' to stop this program.
'''