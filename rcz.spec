# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.


======== SETTINGS ========

Actions: # List of action propositions and their state (enabled = 1, disabled = 0)
shoot_goal, 0
pass_ball, 0
block_goal, 1
steal_ball, 0
play_goalie, 1

CompileOptions:
convexify: True
parser: structured
fastslow: False
decompose: True
use_region_bit_encoding: True

CurrentConfigName:
Untitled configuration

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
attempt3.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)
ball_isnear, 1
has_ball, 0
missing_goalie, 1
roster_swap, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
circle1 = p4
crease1 = p3
crease2 = p2
others = p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19

Spec: # Specification in structured English

#environment starts with not ball_isnear and not roster_swap and not missing_goalie
robot starts in circle1
#robot starts with not block_goal and not play_goalie


play_goalie is set on missing_goalie and reset on roster_swap

if play_goalie then go to crease1 and stay there
do block_goal if and only if play_goalie and you are activating ball_isnear

