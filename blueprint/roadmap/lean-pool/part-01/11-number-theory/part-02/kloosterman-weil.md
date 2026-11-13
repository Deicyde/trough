---
declaration: theorem
origin: cited
lean: KloostermanWeil.weil1948_bound, KloostermanWeil.kloostermanUnitSum_crt, KloostermanWeil.centeredReducedIntervalSum_bound
statement: formalized
proof: formalized
---

# Kloosterman–Weil bounds via Carlitz and Stepanov

> Proves the classical prime Kloosterman–Weil bound by extension-field recurrences and auxiliary-polynomial point counts. Develops exact CRT factorization, squarefree bounds with a unit first coefficient, and centered incomplete reciprocal-phase bounds at the reduced modulus.

*Quoted from the card [LeanPool/projects/kloosterman-weil.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/kloosterman-weil.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`KloostermanWeil.weil1948_bound`](https://leanpool.github.io/lean-pool/LeanPool/KloostermanWeil/Weil/PrimeKloosterman.html#KloostermanWeil.weil1948_bound) (theorem; a main declaration), declared in [LeanPool/KloostermanWeil/Weil/PrimeKloosterman.lean, line 30](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KloostermanWeil/Weil/PrimeKloosterman.lean#L30): “For every prime p and nonzero coefficients m and n modulo p, the norm of the standard Kloosterman sum is at most twice the square root of p.”
- [`KloostermanWeil.kloostermanUnitSum_crt`](https://leanpool.github.io/lean-pool/LeanPool/KloostermanWeil/Weil/ChineseRemainderAndCompletion.html#KloostermanWeil.kloostermanUnitSum_crt) (theorem; a main declaration), declared in [LeanPool/KloostermanWeil/Weil/ChineseRemainderAndCompletion.lean, line 142](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KloostermanWeil/Weil/ChineseRemainderAndCompletion.lean#L142): “Kloosterman sums factor exactly over coprime nonzero moduli, with explicit Bezout-normalized coefficients.”
- [`KloostermanWeil.centeredReducedIntervalSum_bound`](https://leanpool.github.io/lean-pool/LeanPool/KloostermanWeil/Weil/Contracts.html#KloostermanWeil.centeredReducedIntervalSum_bound) (theorem; a main declaration), declared in [LeanPool/KloostermanWeil/Weil/Contracts.lean, line 47](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KloostermanWeil/Weil/Contracts.lean#L47): “For a positive squarefree modulus q, the mean-centered reciprocal phase defined at q divided by gcd(A,q) has interval sums bounded uniformly in interval length by its squarefree Weil constant times one plus log of that reduced modulus.”
- [`KloostermanWeil.squarefreeUnitNumerator_bound`](https://leanpool.github.io/lean-pool/LeanPool/KloostermanWeil/Weil/Contracts.html#KloostermanWeil.squarefreeUnitNumerator_bound) (theorem), declared in [LeanPool/KloostermanWeil/Weil/Contracts.lean, line 27](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KloostermanWeil/Weil/Contracts.lean#L27): “For every nonzero squarefree modulus q and unit first coefficient, the Kloosterman sum is bounded by 2 to the number of prime factors of q times the square root of q.”

## Project

- Authors: Charlie Dorsey.
- Source: *Weil Bounds Toolkit*.
- Project repository: [charliedorsey/weil-bounds-toolkit](https://github.com/charliedorsey/weil-bounds-toolkit), at commit [7adcd236](https://github.com/charliedorsey/weil-bounds-toolkit/tree/7adcd23667b063ae54cc0e8707c89ce259e8fd31).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11L05, 11T23.
- In Lean Pool: [LeanPool/KloostermanWeil](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KloostermanWeil), from the card [LeanPool/projects/kloosterman-weil.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/kloosterman-weil.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/kloosterman-weil.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/kloosterman-weil.yaml)
- [Lean Pool at 701389c0: LeanPool/KloostermanWeil](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KloostermanWeil)
