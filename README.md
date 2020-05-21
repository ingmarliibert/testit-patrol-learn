TestIt Patrol model learning use case
======================

Demonstration of TestIt using the explore and learn functionalities to build the Uppaal model.

```
rosrun testit testit_command.py bringup         # Bring up the pipelines
rosrun testit testit_command.py explore         # Explore the state space of the robotsystem as specified in logger.yaml
rosrun testit testit_command.py learn           # Learn the model as an Uppaal automata from the logfile specified in config.yaml
rosrun testit testit_command.py refine-model    # Refine the model specified in config.yaml and output a new one
rosrun testit testit_command.py test T2         # Runs Uppaal TRON
rosrun testit testit_command.py test T3         # Runs testit_optimizer to find optimized cases
```
