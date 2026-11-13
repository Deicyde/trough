---
declaration: section
origin: cited
lean: StatMech.DeterminedBy, StatMech.determinedBy_iff_dependsOn, StatMech.wprob_inter_eq_mul_of_determined, StatMech.reimer_bernoulli_eq_of_determinedDisjoint
statement: formalized
proof: formalized
---

# Events determined by disjoint coordinate sets

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/events-determined-by-disjoint-coordinate-sets/index.html).

## Event determined by a set of coordinates

`DeterminedBy A K`: whether a configuration lies in `A` depends only on its values on `K`.
This is definitionally `StatMech.DependsOn A K`.

Formalized by `StatMech.DeterminedBy`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDisjointDetermined.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDisjointDetermined.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/events-determined-by-disjoint-coordinate-sets/index.html#determined-by).

## Determined-by and depends-on are the same predicate

`DeterminedBy` and `DependsOn` are the same predicate.

Formalized by `StatMech.determinedBy_iff_dependsOn`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDisjointDetermined.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDisjointDetermined.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/events-determined-by-disjoint-coordinate-sets/index.html#determined-by-iff-depends-on).

## Independence of events determined by disjoint coordinate sets

Events determined by disjoint coordinate sets are independent under a product probability
weight: `wprob φ (A ∩ B) = wprob φ A * wprob φ B`.

Formalized by `StatMech.wprob_inter_eq_mul_of_determined`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDisjointDetermined.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDisjointDetermined.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/events-determined-by-disjoint-coordinate-sets/index.html#wprob-inter-eq-mul-of-determined).

## Reimer equality for events determined by disjoint coordinates

Reimer's inequality with equality for events determined by disjoint coordinate sets: under
the product Bernoulli(`p`) measure, `P_p(A □ B) = P_p(A) * P_p(B)`.

Formalized by `StatMech.reimer_bernoulli_eq_of_determinedDisjoint`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDisjointDetermined.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDisjointDetermined.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/events-determined-by-disjoint-coordinate-sets/index.html#reimer-bernoulli-eq-of-determined-disjoi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Events determined by disjoint coordinate sets](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/events-determined-by-disjoint-coordinate-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/reimer-inequality/events-determined-by-disjoint-coordinate-sets)
