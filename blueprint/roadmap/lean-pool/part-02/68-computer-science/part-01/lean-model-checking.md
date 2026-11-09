---
declaration: theorem
origin: cited
lean: LeanModelChecking.for_any_LTL_formula_exists_an_equivalent_NBW
statement: formalized
proof: formalized
---

# Formalizations of theorems related to model checking

> Proves that every linear temporal logic formula has an equivalent finite-state nondeterministic Büchi automaton (via negation normal form, alternating Büchi automata, and the Miyano-Hayashi breakpoint construction), and that every linear-time property decomposes as the intersection of a safety property and a liveness property.

*Quoted from the card [LeanPool/projects/lean-model-checking.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-model-checking.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanModelChecking.for_any_LTL_formula_exists_an_equivalent_NBW`](https://leanpool.github.io/lean-pool/LeanPool/LeanModelChecking/LTLNBWResult.html#LeanModelChecking.for_any_LTL_formula_exists_an_equivalent_NBW) (theorem; a main declaration), declared in [LeanPool/LeanModelChecking/LTLNBWResult.lean, line 35](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanModelChecking/LTLNBWResult.lean#L35): “For any linear temporal logic formula there exists an equivalent finite-state nondeterministic Büchi automaton, i.e. one whose state type is finite, accepting the same language.” Its source, as the card gives it: “M. Y. Vardi and P. Wolper, An automata-theoretic approach to automatic program verification, LICS 1986, 332-344; C. Baier and J.-P. Katoen, Principles of Model Checking, MIT Press, 2008, ISBN 978-0-262-02649-9, https://mitpress.mit.edu/9780262026499/principles-of-model-checking/”
- [`LeanModelChecking.LTL`](https://leanpool.github.io/lean-pool/LeanPool/LeanModelChecking/LTLNBWStatement.html#LeanModelChecking.LTL) (inductive), declared in [LeanPool/LeanModelChecking/LTLNBWStatement.lean, line 25](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanModelChecking/LTLNBWStatement.lean#L25): “The syntax of linear temporal logic formulas over a set of atomic propositions.”
- [`LeanModelChecking.NBW`](https://leanpool.github.io/lean-pool/LeanPool/LeanModelChecking/LTLNBWStatement.html#LeanModelChecking.NBW) (structure), declared in [LeanPool/LeanModelChecking/LTLNBWStatement.lean, line 48](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanModelChecking/LTLNBWStatement.lean#L48): “A nondeterministic Büchi automaton over a given alphabet of letters.”
- [`LeanModelChecking.ABW.toNBW.lang_eq`](https://leanpool.github.io/lean-pool/LeanPool/LeanModelChecking/ABWNBW.html#LeanModelChecking.ABW.toNBW.lang_eq) (theorem), declared in [LeanPool/LeanModelChecking/ABWNBW.lean, line 323](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanModelChecking/ABWNBW.lean#L323): “The Miyano-Hayashi breakpoint construction turns any alternating Büchi automaton over a finite state space into a nondeterministic Büchi automaton accepting the same language.” Its source, as the card gives it: “S. Miyano and T. Hayashi, Alternating finite automata on omega-words, Theoretical Computer Science 32 (1984), 321-330, doi:10.1016/0304-3975(84)90049-5”
- [`SafetyLivenessDecomposition.safety_liveness_decomposition`](https://leanpool.github.io/lean-pool/LeanPool/LeanModelChecking/SafetyLivenessDecomposition.html#SafetyLivenessDecomposition.safety_liveness_decomposition) (theorem), declared in [LeanPool/LeanModelChecking/SafetyLivenessDecomposition.lean, line 99](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanModelChecking/SafetyLivenessDecomposition.lean#L99): “Every linear-time property is the intersection of a safety property and a liveness property.” Its source, as the card gives it: “B. Alpern and F. B. Schneider, Defining liveness, Information Processing Letters 21 (1985), 181-185, doi:10.1016/0020-0190(85)90056-0”

## Project

- Authors: György Kurucz.
- Source: *An Automata-Theoretic Approach to Linear Temporal Logic* by Moshe Y. Vardi, [doi:10.1007/3-540-60915-6_6](https://doi.org/10.1007/3-540-60915-6_6).
- Project repository: [kuruczgy/lean-model-checking](https://github.com/kuruczgy/lean-model-checking).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 68Q60, 03B44, 68Q45.
- In Lean Pool: [LeanPool/LeanModelChecking](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanModelChecking), from the card [LeanPool/projects/lean-model-checking.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-model-checking.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/lean-model-checking.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-model-checking.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LeanModelChecking](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanModelChecking)
