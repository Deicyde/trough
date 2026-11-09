---
declaration: theorem
origin: cited
lean: Erdos478.erdos_478
statement: formalized
---

# Erdős Problem 478

> *References:*
> - [erdosproblems.com/478](https://www.erdosproblems.com/478)
> - [AnTa16] V. Andrejić and M. Tatarevic, *On distinct residues of factorials*. arXiv:1603.04086
>   (2016).
> - [GSSV24] Grebennikov, Alexandr and Sagdeev, Arsenii and Semchankau, Aliaksei and Vasilevskii,
>   Aliaksei, *On the sequence {$n! \bmod p$}*. Rev. Mat. Iberoam. (2024), 637--648.
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.
> - [KlMu17] Klurman, Oleksiy and Munsch, Marc, *Distribution of factorials modulo {$p$}*. J. Théor.
>   Nombres Bordeaux (2017), 169--177.
> - [RoSc60] Rokowska, B. and Schinzel, A., *Sur un problème de {M}. {E}rdős*. Elem. Math. (1960),
>   84--85.
> - [Tr13] T. Trudgian, *There are no socialist primes less than $10^9$*. arXiv:1310.6403 (2013).

*Quoted from [FormalConjectures/ErdosProblems/478.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/478.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/478](https://www.erdosproblems.com/478).

The file states 1 research or textbook statement: 1 open.

## `Erdos478.erdos_478`

Open: stated without proof.

> Let $p$ be a prime and
>
> $$A_p = \{ k! \pmod{p} : 1\leq k\lt p\}.$$
>
> Is it true that
>
> $$\lvert A_p\rvert \sim (1-\tfrac{1}{e})p?$$

```lean
theorem erdos_478 :
    Filter.Tendsto
      (fun p : ℕ =>
        (((Finset.Ico 1 p).image (fun k => Nat.factorial k % p)).card : ℝ) / p)
      (Filter.atTop ⊓ Filter.principal {p : ℕ | p.Prime})
      (nhds (1 - 1 / Real.exp 1))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/478.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/478.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/478.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/478.lean)
- [erdosproblems.com/478](https://www.erdosproblems.com/478)
