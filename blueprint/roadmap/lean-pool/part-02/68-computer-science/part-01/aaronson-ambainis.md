---
declaration: theorem
origin: cited
lean: AaronsonAmbainis.aaronson_ambainis, AaronsonAmbainis.aaronson_ambainis_explicit, AaronsonAmbainis.aaronson_ambainis_pm
statement: formalized
proof: formalized
---

# The Aaronson–Ambainis influence conjecture

> Proves that a real polynomial of degree at most d, bounded between zero and one on the Boolean cube and with variance at least epsilon > 0, has a coordinate of squared-difference influence at least (epsilon/d)^7. Also proves explicit bounds with epsilon^(5/2)/d^6, together with determinant pairings, fractional-certificate inequalities and coordinate averaging. The internal packing-cover duality supports the proof; generic finite LP duality is already pooled as StandardLP.strongDuality. The sharper constant is conditional on the stated Agarwal–Ben-David fractional block-sensitivity bound. Quantum simulation consequences are outside this formalization.

*Quoted from the card [LeanPool/projects/aaronson-ambainis.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/aaronson-ambainis.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`AaronsonAmbainis.aaronson_ambainis`](https://leanpool.github.io/lean-pool/LeanPool/AaronsonAmbainis/Main.html#AaronsonAmbainis.aaronson_ambainis) (theorem; a main declaration), declared in [LeanPool/AaronsonAmbainis/Main.lean, line 44](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AaronsonAmbainis/Main.lean#L44): “For every real polynomial in N variables of total degree at most d, bounded between zero and one on the Boolean cube, positive variance at least epsilon guarantees a coordinate whose uniform mean squared change under a bit flip is at least (epsilon/d)^7.”
- [`AaronsonAmbainis.aaronson_ambainis_explicit`](https://leanpool.github.io/lean-pool/LeanPool/AaronsonAmbainis/Main.html#AaronsonAmbainis.aaronson_ambainis_explicit) (theorem; a main declaration), declared in [LeanPool/AaronsonAmbainis/Main.lean, line 49](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AaronsonAmbainis/Main.lean#L49): “Under the same hypotheses, a coordinate has squared-difference influence at least 8 sqrt(15) epsilon^(5/2) / (125 pi^4 d^6).”
- [`AaronsonAmbainis.aaronson_ambainis_pm`](https://leanpool.github.io/lean-pool/LeanPool/AaronsonAmbainis/Main.html#AaronsonAmbainis.aaronson_ambainis_pm) (theorem; a main declaration), declared in [LeanPool/AaronsonAmbainis/Main.lean, line 54](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AaronsonAmbainis/Main.lean#L54): “For a real polynomial of degree at most d bounded in absolute value by one on the sign cube, positive variance at least epsilon guarantees a coordinate whose uniform mean squared half-difference under a bit flip is at least sqrt(15) epsilon^(5/2) / (500 pi^4 d^6).”
- [`AaronsonAmbainis.aaronson_ambainis_of_fbsDegreeBound`](https://leanpool.github.io/lean-pool/LeanPool/AaronsonAmbainis/Main.html#AaronsonAmbainis.aaronson_ambainis_of_fbsDegreeBound) (theorem), declared in [LeanPool/AaronsonAmbainis/Main.lean, line 59](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AaronsonAmbainis/Main.lean#L59): “Assuming the explicitly stated Agarwal–Ben-David fractional block-sensitivity bound, the zero-one cube influence bound improves to 32 sqrt(15) epsilon^(5/2) / (125 pi^4 d^6).”

## Project

- Authors: David Turturean.
- Source: *A proof of the Aaronson–Ambainis conjecture*.
- Project repository: [physical-superintelligence/aaronson-ambainis](https://github.com/physical-superintelligence/aaronson-ambainis), at commit [2a6ceaef](https://github.com/physical-superintelligence/aaronson-ambainis/tree/2a6ceaef872ae993708950f951989134084b851a).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q12, 60C05, 05D40.
- In Lean Pool: [LeanPool/AaronsonAmbainis](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AaronsonAmbainis), from the card [LeanPool/projects/aaronson-ambainis.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/aaronson-ambainis.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/aaronson-ambainis.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/aaronson-ambainis.yaml)
- [Lean Pool at 2b205bf9: LeanPool/AaronsonAmbainis](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AaronsonAmbainis)
