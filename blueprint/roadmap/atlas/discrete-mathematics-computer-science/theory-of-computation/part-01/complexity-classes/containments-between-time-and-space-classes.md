---
declaration: section
origin: cited
lean: Cslib.Turing.MultiTapeTM.haltTime_lt_coreBound, Cslib.Turing.MultiTapeTM.runsInTime_coreBound, Cslib.Turing.MultiTapeTM.runsInTime_exponential_of_space, Cslib.Turing.MultiTapeTM.exists_exponential_time_bound, Cslib.Turing.MultiTapeTM.SpaceBoundedBy.exists_exponential_timeBoundedBy, MetaMathlibExt.Complexity.KeyTheorems.PSPACESubsetEXP.pspace_subset_exp, MetaMathlibExt.Complexity.KeyTheorems.NEXPSubsetEXPSPACE.nexp_subset_expspace, MetaMathlibExt.Complexity.KeyTheorems.NLSubsetP.nl_subset_p
statement: formalized
---

# Containments between time and space classes

9 results, 6 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html).

## First halting time is below the configuration-core bound

The first halting time is smaller than the canonical bound on reachable cores.

Formalized by `Cslib.Turing.MultiTapeTM.haltTime_lt_coreBound`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeFromSpace.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/TimeFromSpace.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html#halt-time-lt-core-bound).

## Halting space-bounded runs obey the core-count time bound

A halting, space-bounded run has an actual step bound.

Formalized by `Cslib.Turing.MultiTapeTM.runsInTime_coreBound`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeFromSpace.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/TimeFromSpace.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html#runs-in-time-core-bound).

## Exponential time bound from a space bound and halting

Exponential time from a visited-cell space bound and a halting run.

Formalized by `Cslib.Turing.MultiTapeTM.runsInTime_exponential_of_space`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeFromSpace.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/TimeFromSpace.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html#runs-in-time-exponential-of-space).

## Uniform constants for the exponential time-from-space bound

One pair of constants works for every input of the fixed machine.

Formalized by `Cslib.Turing.MultiTapeTM.exists_exponential_time_bound`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeFromSpace.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/TimeFromSpace.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html#exists-exponential-time-bound).

## Polynomial-space decider runs in exponential time

The same finite polynomial-space decider has an exponential time bound.
All constants precede every input. Halting comes from `Decides`, not space.

Formalized by `Cslib.Turing.MultiTapeTM.SpaceBoundedBy.exists_exponential_timeBoundedBy`, a theorem declared in [CSLibExt/Computability/Complexity/SpaceInclusions.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SpaceInclusions.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html#exists-exponential-time-bounded-by).

## PSPACE is contained in EXP

Every canonical polynomial-space language is in exponential time,
using its original finite multi-tape decider.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, Cambridge University Press, 2009, Chapter 4 (Space complexity).

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.PSPACESubsetEXP.pspace_subset_exp`, a theorem declared in [CSLibExt/Computability/Complexity/SpaceInclusions.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SpaceInclusions.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html#pspace-subset-exp).

## NEXP is contained in EXPSPACE

Every decision problem in NEXP, the class of
nondeterministic exponential time, also belongs to EXPSPACE, the class of deterministic
exponential space.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009 (NEXP ⊆ EXPSPACE by exhaustive simulation).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.NEXPSubsetEXPSPACE.nexp_subset_expspace` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/NEXPSubsetEXPSPACEWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/NEXPSubsetEXPSPACEWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html#nexp-subset-expspace).

## NL is contained in P

Every decision problem in NL, the class of nondeterministic
logarithmic space, also belongs to P, the class of decision problems computable in deterministic
polynomial time.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Theorem 4.14 (NL ⊆ P); C. H. Papadimitriou, Computational Complexity, 1994.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.NLSubsetP.nl_subset_p` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/NLSubsetPWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/NLSubsetPWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html#nl-subset-p).

## NP is contained in PSPACE

Every decision problem in NP also belongs to PSPACE, the class
of decision problems decidable in polynomial space.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, Cambridge University Press, 2009, Theorem 4.14 (NP ⊆ PSPACE); C. H. Papadimitriou, Computational Complexity, Addison-Wesley, 1994, Theorem 7.2.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.NPSubsetPSPACE.np_subset_pspace` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/NPSubsetPSPACEWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/NPSubsetPSPACEWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html#np-subset-pspace).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Containments between time and space classes](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/complexity-classes/containments-between-time-and-space-classes)
