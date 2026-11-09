---
declaration: theorem
origin: cited
lean: WieferichMirimanoffPrime.exists_isWieferichPrime_and_isMirimanoffPrime, WieferichMirimanoffPrime.isMirimanoffPrime_iff
statement: formalized
---

# Can a prime $p$ satisfy $2^{p-1} \equiv 1 \pmod{p^2}$ and $3^{p-1} \equiv 1 \pmod{p^2}$?

> A prime $p$ with $2^{p-1} \equiv 1 \pmod{p^2}$ is a Wieferich prime (the only known examples
> are $1093$ and $3511$). A prime $p$ with $3^{p-1} \equiv 1 \pmod{p^2}$ is a Mirimanoff prime
> (the only known examples are $11$ and $1006003$). It is an open question whether a prime can
> satisfy both congruences simultaneously. Lenstra gave a heuristic argument against this.
>
> *References:*
> * [Wikipedia, List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)
> * [Wikipedia, Wieferich prime](https://en.wikipedia.org/wiki/Wieferich_prime)
> * J. B. Dobson, [On Lerch's formula for the Fermat quotient](https://arxiv.org/abs/1103.3907v6)
> * F. G. Dorais and D. Klyve, [A Wieferich prime search up to $6.7 \times 10^{15}$](https://cs.uwaterloo.ca/journals/JIS/VOL14/Klyve/klyve3.html),
>   J. Integer Seq. 14 (2011), Article 11.9.2.
> * [OEIS A001220](https://oeis.org/A001220) (Wieferich primes)
> * [OEIS A014127](https://oeis.org/A014127) (Mirimanoff primes)

*Quoted from [FormalConjectures/Wikipedia/WieferichMirimanoffPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WieferichMirimanoffPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 4 test statements, counted here but not shown.

## `WieferichMirimanoffPrime.exists_isWieferichPrime_and_isMirimanoffPrime`

Open: stated without proof.

> Can a prime $p$ satisfy $2^{p-1} \equiv 1 \pmod{p^2}$ and $3^{p-1} \equiv 1 \pmod{p^2}$
> simultaneously? That is, does there exist a prime $p$ that is both a Wieferich prime and a
> Mirimanoff prime? Wikipedia's list of unsolved problems poses this question, citing
> J. B. Dobson, [On Lerch's formula for the Fermat quotient](https://arxiv.org/abs/1103.3907v6).
> Lenstra gave a heuristic argument against the existence of such a prime (see Dobson, Section 9).

```lean
theorem exists_isWieferichPrime_and_isMirimanoffPrime :
    ∃ p : ℕ, IsWieferichPrime p ∧ IsMirimanoffPrime p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WieferichMirimanoffPrime.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WieferichMirimanoffPrime.lean#L50).

## `WieferichMirimanoffPrime.isMirimanoffPrime_iff`

Open: stated without proof.

> Are $11$ and $1006003$ the only Mirimanoff primes? They are the only known ones: Dorais and Klyve
> found no other below $9.7 \times 10^{14}$.

```lean
theorem isMirimanoffPrime_iff :
    ∀ p, IsMirimanoffPrime p ↔ p = 11 ∨ p = 1006003
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WieferichMirimanoffPrime.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WieferichMirimanoffPrime.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/WieferichMirimanoffPrime.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WieferichMirimanoffPrime.lean)
- [Wikipedia, List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)
