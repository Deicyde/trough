---
declaration: theorem
origin: cited
lean: flt_regular
statement: formalized
proof: formalized
---

# Fermat's Last Theorem for regular primes

> Formalizes Kummer's proof of Fermat's Last Theorem for every odd regular prime exponent. The development proves both cases of the theorem and includes the required theory of cyclotomic integers, relative units, Hilbert 90 and 92, ramification, class groups, and Kummer's lemma.

*Quoted from the card [LeanPool/projects/flt-regular.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/flt-regular.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`flt_regular`](https://leanpool.github.io/lean-pool/LeanPool/FltRegular/FltRegular.html#flt_regular) (theorem; a main declaration), declared in [LeanPool/FltRegular/FltRegular.lean, line 27](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FltRegular/FltRegular.lean#L27): “Fermat's Last Theorem holds for every odd regular prime exponent.”
- [`FltRegular.caseI`](https://leanpool.github.io/lean-pool/LeanPool/FltRegular/CaseI/Statement.html#FltRegular.caseI) (theorem), declared in [LeanPool/FltRegular/CaseI/Statement.lean, line 279](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FltRegular/CaseI/Statement.lean#L279): “The first case of Fermat's Last Theorem holds for every regular prime: no primitive solution exists when the exponent does not divide the product of the three terms.”
- [`FltRegular.caseII`](https://leanpool.github.io/lean-pool/LeanPool/FltRegular/CaseII/Statement.html#FltRegular.caseII) (theorem), declared in [LeanPool/FltRegular/CaseII/Statement.lean, line 95](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FltRegular/CaseII/Statement.lean#L95): “The second case of Fermat's Last Theorem holds for every odd regular prime: no primitive nonzero solution exists when the exponent divides the product of the three terms.”
- [`eq_pow_prime_of_unit_of_congruent`](https://leanpool.github.io/lean-pool/LeanPool/FltRegular/NumberTheory/KummersLemma/KummersLemma.html#eq_pow_prime_of_unit_of_congruent) (theorem), declared in [LeanPool/FltRegular/NumberTheory/KummersLemma/KummersLemma.lean, line 63](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FltRegular/NumberTheory/KummersLemma/KummersLemma.lean#L63): “A unit of the cyclotomic field of an odd regular prime that is congruent to an integer modulo the prime is itself a prime-th power.”

## Project

- Authors: FltRegular contributors.
- Source: *Fermat's Last Theorem for regular primes* by Riccardo Brasca, Ruben Van de Velde, Andrew Yang, Chris Birkbeck, Alex J. Best, Eric Rodriguez.
- Project repository: [leanprover-community/flt-regular](https://github.com/leanprover-community/flt-regular), at commit [94a1d789](https://github.com/leanprover-community/flt-regular/tree/94a1d78956a348568c80975ec9005dc5762ab10a).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11D41, 11R18, 11R29.
- In Lean Pool: [LeanPool/FltRegular](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FltRegular), from the card [LeanPool/projects/flt-regular.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/flt-regular.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/flt-regular.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/flt-regular.yaml)
- [Lean Pool at 2b205bf9: LeanPool/FltRegular](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FltRegular)
