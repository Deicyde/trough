---
declaration: section
origin: cited
lean: StatMech.isLowerSet_iff_isDownAt_all, StatMech.familyEvent, StatMech.reimer_wprob_familyEvent_of_isLowerSet, StatMech.reimer_wprob_familyEvent_of_isUpperSet
statement: formalized
proof: formalized
---

# Families of finsets as events

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/families-of-finsets-as-events/index.html).

## Lower sets are families closed under erasing an element

A family of finsets is a lower set iff it is closed under erasing any single element.

Formalized by `StatMech.isLowerSet_iff_isDownAt_all`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerFamilyEvents.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerFamilyEvents.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/families-of-finsets-as-events/index.html#is-lower-set-iff-is-down-at-all).

## Event of a family of finsets

The event that the support of a configuration lies in the family `𝒜`.

Formalized by `StatMech.familyEvent`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerFamilyEvents.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerFamilyEvents.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/families-of-finsets-as-events/index.html#family-event).

## Reimer's inequality for two lower families

Reimer's inequality for the events of two lower families (the BK inequality for
decreasing events).

Formalized by `StatMech.reimer_wprob_familyEvent_of_isLowerSet`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerFamilyEvents.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerFamilyEvents.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/families-of-finsets-as-events/index.html#reimer-wprob-family-event-of-is-lower-se).

## Reimer's inequality for two upper families

Reimer's inequality for the events of two upper families (the BK inequality).

Formalized by `StatMech.reimer_wprob_familyEvent_of_isUpperSet`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerFamilyEvents.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerFamilyEvents.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/families-of-finsets-as-events/index.html#reimer-wprob-family-event-of-is-upper-se).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Families of finsets as events](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/families-of-finsets-as-events/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/reimer-inequality/families-of-finsets-as-events)
