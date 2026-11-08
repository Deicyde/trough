---
declaration: theorem
origin: cited
lean: Erdos367.erdos_367_k3, RFullOdd.erdos367_iv, Erdos367.erdos367
statement: formalized
proof: formalized
---

# Erdős Problem \#367

> Formalizes upper and lower bound results for powerful parts of products of consecutive integers, including abc-conditional upper bounds, an unconditional odd r-full lower bound, a Pell-style limsup theorem, and polynomial arithmetic cores.

*Quoted from the card [LeanPool/projects/erdos367.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos367.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Erdos367.erdos_367_k3`](https://leanpool.github.io/lean-pool/LeanPool/Erdos367/K3AbcUpperBound.html#Erdos367.erdos_367_k3) (theorem; a main declaration), declared in [LeanPool/Erdos367/K3AbcUpperBound.lean, line 381](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos367/K3AbcUpperBound.lean#L381): “Proves an abc-conditional k = 3 upper bound for the product of square-full parts of three consecutive integers.”
- [`GeneralK.B2_upper_bound`](https://leanpool.github.io/lean-pool/LeanPool/Erdos367/GeneralKUpperBound.html#GeneralK.B2_upper_bound) (theorem), declared in [LeanPool/Erdos367/GeneralKUpperBound.lean, line 160](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos367/GeneralKUpperBound.lean#L160): “Proves a general-k upper bound for the square-full part of a product of consecutive integers from an explicit radical lower-bound hypothesis.”
- [`RFullOdd.erdos367_iv`](https://leanpool.github.io/lean-pool/LeanPool/Erdos367/RFullLowerBound.html#RFullOdd.erdos367_iv) (theorem; a main declaration), declared in [LeanPool/Erdos367/RFullLowerBound.lean, line 184](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos367/RFullLowerBound.lean#L184): “Gives an unconditional odd r construction where the product of r-full parts of two consecutive integers is larger than the stated power of n.”
- [`Erdos367.erdos367`](https://leanpool.github.io/lean-pool/LeanPool/Erdos367/PellLimsup.html#Erdos367.erdos367) (theorem; a main declaration), declared in [LeanPool/Erdos367/PellLimsup.lean, line 903](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos367/PellLimsup.lean#L903): “Proves an unconditional limsup form showing that the product of square-full parts of three consecutive integers exceeds any fixed multiple of n squared times log n.”
- [`Core139.T3`](https://leanpool.github.io/lean-pool/LeanPool/Erdos367/Core139.html#Core139.T3) (theorem), declared in [LeanPool/Erdos367/Core139.lean, line 200](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos367/Core139.lean#L200): “Proves the integer-form arithmetic core yielding the E3 at least 13/9 lower-bound construction under explicit prime-supply data.”
- [`Core4027.IDENT`](https://leanpool.github.io/lean-pool/LeanPool/Erdos367/Core4027.html#Core4027.IDENT) (theorem), declared in [LeanPool/Erdos367/Core4027.lean, line 95](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos367/Core4027.lean#L95): “Verifies the degree-27 polynomial identity used in the Davenport-Zannier construction.”
- [`Core4027.T3`](https://leanpool.github.io/lean-pool/LeanPool/Erdos367/Core4027.html#Core4027.T3) (theorem), declared in [LeanPool/Erdos367/Core4027.lean, line 343](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos367/Core4027.lean#L343): “Proves the integer-form arithmetic core yielding the E3 at least 40/27 lower-bound construction under explicit prime-supply data.”

## Project

- Authors: Scott D. Hughes.
- Source: *Powerful parts of consecutive integers and Davenport-Zannier polynomials* by Scott D. Hughes.
- Project repository: [scottdhughes/erdos367](https://github.com/scottdhughes/erdos367).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11D09, 11N25, 11D45.
- In Lean Pool: [LeanPool/Erdos367](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos367), from the card [LeanPool/projects/erdos367.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos367.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/erdos367.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos367.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Erdos367](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos367)
