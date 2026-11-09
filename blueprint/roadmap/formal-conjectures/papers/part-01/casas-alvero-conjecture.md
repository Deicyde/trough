---
declaration: theorem
origin: cited
lean: CasasAlvero.casas_alvero_conjecture, CasasAlvero.casas_alvero.prime_power, CasasAlvero.casas_alvero.double_prime_power, CasasAlvero.casas_alvero.positive_char_counterexample
statement: formalized
---

# Casas-Alvero Conjecture

> *References:*
> * [The Casas-Alvero conjecture for infinitely many degrees](https://arxiv.org/pdf/math/0605090)
> * [MathOverflow](https://mathoverflow.net/questions/27851)
>
> The Casas-Alvero conjecture states that if a univariate polynomial `P` of degree `d` over a field
> of characteristic zero shares a non-trivial factor with its Hasse derivatives up to order `d-1`,
> then `P` must be of the form `(X - α)ᵈ` for some `α` in the field.
>
> The conjecture has been proven for:
> * Degrees `d ≤ 8`
> * Degrees of the form `p^k` where `p` is prime
> * Degrees of the form `2p^k` where `p` is prime
>
> The conjecture is false in positive characteristic `p` for polynomials of degree `p+1`.
>
> The conjecture is now claimed to be proven in this paper:
> * [Proof of the Casas-Alvero conjecture: Soham Ghosh)](https://arxiv.org/pdf/2501.09272)

*Quoted from [FormalConjectures/Paper/CasasAlvero.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/CasasAlvero.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 4 API statements, counted here but not shown.

## `CasasAlvero.casas_alvero_conjecture`

Open: stated without proof.

> The Casas-Alvero conjecture states that in characteristic zero, if a monic polynomial `P`
> has the Casas-Alvero property, then `P = (X - α)ᵈ` for some `α`.

```lean
theorem casas_alvero_conjecture (hP' : HasCasasAlveroProp P) :
    ∃ α : K, P = (X - C α) ^ P.natDegree
```

Category `research open`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/CasasAlvero.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/CasasAlvero.lean#L124).

## `CasasAlvero.casas_alvero.prime_power`

Solved: stated here without proof.

> The Casas-Alvero conjecture holds for polynomials of prime power degree.
> This was proved by Graf von Bothmer, Labs, Schicho, and van de Woestijne.
>
> Reference: [The Casas-Alvero conjecture for infinitely many degrees](https://arxiv.org/pdf/math/0605090)

```lean
theorem casas_alvero.prime_power (p k : ℕ) (hp : p.Prime) (hd : P.natDegree = p^k)
    (hP' : HasCasasAlveroProp P) : ∃ α : K, P = (X - C α) ^ P.natDegree
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/CasasAlvero.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/CasasAlvero.lean#L135).

## `CasasAlvero.casas_alvero.double_prime_power`

Solved: stated here without proof.

> The Casas-Alvero conjecture holds for polynomials of degree `2p^k` where `p` is prime.
> This was proved by Graf von Bothmer, Labs, Schicho, and van de Woestijne.
>
> Reference: [The Casas-Alvero conjecture for infinitely many degrees](https://arxiv.org/pdf/math/0605090)

```lean
theorem casas_alvero.double_prime_power (p k : ℕ) (hp : p.Prime) (hd : P.natDegree = 2 * p^k)
    (hP' : HasCasasAlveroProp P) : ∃ α : K, P = (X - C α) ^ P.natDegree
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/CasasAlvero.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/CasasAlvero.lean#L146).

## `CasasAlvero.casas_alvero.positive_char_counterexample`

Solved: stated here; a Lean proof is at [https://github.com/mzhorvath1/formal-conjectures/blob/4f2343508f2c157f35abb7be4814bd550280ce81/FormalConjectures/Paper/CasasAlvero.lean#163](https://github.com/mzhorvath1/formal-conjectures/blob/4f2343508f2c157f35abb7be4814bd550280ce81/FormalConjectures/Paper/CasasAlvero.lean#163).

> The Casas-Alvero conjecture fails in positive characteristic `p` for polynomials of degree `p + 1`.
> This was shown by Graf von Bothmer, Labs, Schicho, and van de Woestijne.
>
> Reference: [The Casas-Alvero conjecture for infinitely many degrees](https://arxiv.org/pdf/math/0605090)
>
> Formal proof linked here provided by AlphaProof.

```lean
theorem casas_alvero.positive_char_counterexample {p : ℕ} (hp : p.Prime) :
    ∃ (K : Type*) (_ : Field K) (_ : CharP K p),
      let P := X ^ (p + 1) - X ^ p
      Monic P ∧ HasCasasAlveroProp P ∧
      ¬∃ α : K, P = (X - C α) ^ P.natDegree
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/CasasAlvero.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/CasasAlvero.lean#L162).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/CasasAlvero.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/CasasAlvero.lean)
- [The Casas-Alvero conjecture for infinitely many degrees](https://arxiv.org/pdf/math/0605090)
