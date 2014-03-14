# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.


======== SETTINGS ========

Actions: # List of action propositions and their state (enabled = 1, disabled = 0)
shoot_goal, 0
pass_ball, 0
block_goal, 1
steal_ball, 0
play_goalie, 1
initial, 1
other_color, 1
penalized, 1
ready, 1
set_state, 0
playing, 0

CompileOptions:
convexify: True
parser: structured
fastslow: False
decompose: True
use_region_bit_encoding: True

CurrentConfigName:
Default configuration

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
attempt7.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)
ball_isnear, 1
has_ball, 0
missing_goalie, 1
roster_swap, 1
left_foot_bump, 1
chest_button, 1
ref_signal, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
penalty_area2 = p10
penalty_area1 = p11
others = p2, p3, p19, p20, p21, p22, p23, p24, p25, p26
sideline1 = p7
circle = p16, p17, p18, p54, p55
side2 = p16, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37
sideline2 = p6
side1 = p17, p18, p38, p39, p40, p41, p42, p43, p44, p45, p46, p47, p48, p49, p50, p51, p52, p53

Spec: # Specification in structured English

#initialization
robot starts in sideline1
robot starts with initial

#actions from the initial state


other_color is set on left_foot_bump and reset on not left_foot_bump

penalized is set on (chest_button and initial) and reset on (not chest_button and not initial)

do initial if and only if (not penalized and not ready) and you are in (sideline1 or sideline2)


#end initial

#ready state

ready is set on (ref_signal and initial) and reset on not ref_signal

go to circle
#end ready

#set state
#do set_state if and only if you are not activating playing and you are in circle

#end set state

#goalie rules
play_goalie is set on missing_goalie and reset on roster_swap

if play_goalie then go to penalty_area1 and stay there
do block_goal if and only if play_goalie and you are activating ball_isnear
#end goalie rules

