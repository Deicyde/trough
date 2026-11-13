---
declaration: theorem
origin: cited
lean: CongruenceNormalizers.newman_iff, CongruenceNormalizers.newman_delta
statement: formalized
proof: formalized
---

# Newman normalizer bounds for congruence subgroups

> Characterizes the normalizer of Gamma0(N) in SL(2, R), for every positive level N, by explicit integral matrices scaled by a square root. Extends the necessary matrix form to GammaDelta(N) for every subgroup Delta of the units modulo N. Preserves Atkin-Lehner elements, rational representatives, integral matrix lattices, prime valuations and a generic normalizer argument. The upstream finite presentations, group orders and modular-curve automorphism classifications are outside this import's scope.

*Quoted from the card [LeanPool/projects/congruence-normalizers.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/congruence-normalizers.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`CongruenceNormalizers.newman_iff`](https://leanpool.github.io/lean-pool/LeanPool/CongruenceNormalizers.html#CongruenceNormalizers.newman_iff) (theorem; a main declaration), declared in [LeanPool/CongruenceNormalizers.lean, line 36](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CongruenceNormalizers.lean#L36): “For N > 0, put h = 2^min(3, floor(v_2(N)/2)) times 3^min(1, floor(v_3(N)/2)) and n = N/h^2. A real determinant-one matrix normalizes Gamma0(N) exactly when it equals plus or minus 1/sqrt(e) times [[a\*e, b/h], [N\*c/h, d\*e]], for integers a, b, c, d and a positive divisor e of n satisfying a\*d\*e^2 - b\*c\*n = e.”
- [`CongruenceNormalizers.newman_delta`](https://leanpool.github.io/lean-pool/LeanPool/CongruenceNormalizers.html#CongruenceNormalizers.newman_delta) (theorem; a main declaration), declared in [LeanPool/CongruenceNormalizers.lean, line 41](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CongruenceNormalizers.lean#L41): “For N > 0 and Delta a subgroup of the units modulo N, let epsilon be gcd(N, u^2 - 1 for representatives u in Delta), and let h be the product over primes p dividing N of p^min(v_p(epsilon), floor(v_p(N)/2)). Every determinant-one real matrix normalizing GammaDelta(N) has the same integral Newman form with this h and n = N/h^2. This is a necessary bound; no converse for GammaDelta(N) is asserted.”
- [`CongruenceNormalizers.hPart_isGreatest'`](https://leanpool.github.io/lean-pool/LeanPool/CongruenceNormalizers/NormalizerLean/Basic.html#CongruenceNormalizers.hPart_isGreatest') (theorem), declared in [LeanPool/CongruenceNormalizers/NormalizerLean/Basic.lean, line 199](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CongruenceNormalizers/NormalizerLean/Basic.lean#L199): “At every positive level, h(N) is the greatest divisor of 24 whose square divides N.”

## Project

- Authors: Filip Najman.
- Source: *The normalizer of Gamma0(N) in PSL(2, R)* by M. Akbas, D. Singerman, [doi:10.1017/S001708950000940X](https://doi.org/10.1017/S001708950000940X).
- Project repository: [F-Najman/normalizer-lean](https://github.com/F-Najman/normalizer-lean), at commit [ea4445c0](https://github.com/F-Najman/normalizer-lean/tree/ea4445c0d991a65d54fc77af0af559f2322e8660).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11F06, 20H05.
- In Lean Pool: [LeanPool/CongruenceNormalizers](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CongruenceNormalizers), from the card [LeanPool/projects/congruence-normalizers.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/congruence-normalizers.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/congruence-normalizers.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/congruence-normalizers.yaml)
- [Lean Pool at 701389c0: LeanPool/CongruenceNormalizers](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CongruenceNormalizers)
