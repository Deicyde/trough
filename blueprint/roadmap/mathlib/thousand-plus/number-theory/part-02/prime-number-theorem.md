# Prime number theorem

Mathlib records this with 2 declarations.

`Nat.isEquivalent_primeCounting`: **The prime number theorem**: the prime counting function satisfies `π x ~ x / Real.log x`.

```lean
Nat.isEquivalent_primeCounting :
  Asymptotics.IsEquivalent Filter.atTop (fun x => ↑⌊x⌋₊.primeCounting) fun x => x / Real.log x
```

`Chebyshev.isEquivalent_theta_id`: **The prime number theorem, `θ` form**: `θ x ~ x`, where `θ x = ∑ p ≤ x, log p` (over
primes `p`) is the Chebyshev function `Chebyshev.theta`.

```lean
Chebyshev.isEquivalent_theta_id : Asymptotics.IsEquivalent Filter.atTop Chebyshev.theta id
```

Mathlib's 1000+ list links a formalization.

Ongoing formalisation of various versions in <https://github.com/AlexKontorovich/PrimeNumberTheoremAnd>.

## Depends on

- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Logarithm](../../../overview/analysis/special-functions/logarithm.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Arithmetic functions](../../../overview/general-algebra/number-theory/arithmetic-functions.md)
- [Euler's totient function ($\varphi$)](../../../overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)
- [Fundamental theorem of algebra](../../../overview/analysis/complex-analysis/fundamental-theorem-of-algebra.md)

## Sources

- [Mathlib documentation: `Nat.isEquivalent_primeCounting`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/WeakPNT.html#Nat.isEquivalent_primeCounting)
- [Source of `Nat.isEquivalent_primeCounting` in Mathlib/NumberTheory/LSeries/WeakPNT.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/NumberTheory/LSeries/WeakPNT.lean#L142)
- [Mathlib documentation: `Chebyshev.isEquivalent_theta_id`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/WeakPNT.html#Chebyshev.isEquivalent_theta_id)
- [Source of `Chebyshev.isEquivalent_theta_id` in Mathlib/NumberTheory/LSeries/WeakPNT.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/NumberTheory/LSeries/WeakPNT.lean#L100)
- [1000+ theorems list: Q386292](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L416)
- [1000+ theorems project: Q386292](https://1000-plus.github.io/all.html?length=-1#Q386292)
- [Wikipedia: Prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem)
- [Wikidata: Q386292](https://www.wikidata.org/wiki/Q386292)
- [Formalization linked by the 1000+ list](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd)
