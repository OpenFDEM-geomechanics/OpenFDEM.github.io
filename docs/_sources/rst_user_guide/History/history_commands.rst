History command overview
========================

The current parser supports history commands beyond the ``pv.*`` export
commands documented on the older pages. The available families include:

- nodal force, internal force, cohesive force and contact force histories;
- nodal displacement, velocity, kinetic energy and group-based variants;
- element stress, strain, strain rate, plastic and energy histories;
- cohesive displacement, force, velocity, shear-strength and energy histories;
- pressure and temperature histories for the coupled modules;
- global fracture, damage, acoustic-emission and energy histories;
- ``interval``, ``pv.interval``, ``pv.dynamic.interval`` and ``write`` controls.

The parser source also contains compatibility spellings such as
``nodal.farcture.pressure.by.group`` and ``element.palstic.by.group``.
These spellings should be tested with the current executable before being
advertised as stable input syntax.

See the individual ``of.history.pv.*`` pages for ParaView exports.
