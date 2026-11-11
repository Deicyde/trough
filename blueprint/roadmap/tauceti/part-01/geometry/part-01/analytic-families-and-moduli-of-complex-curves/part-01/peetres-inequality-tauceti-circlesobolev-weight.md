---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.weight_add_le
statement: formalized
proof: formalized
---

# Peetre's inequality (`TauCeti.CircleSobolev.weight_add_le`)

`(1 + |m + n|) ^ s ≤ (1 + |m|) ^ |s| (1 + |n|) ^ s` for every real
`s`. Shifting frequencies by `m` therefore changes the weights of every order `s` by at most the
factor `(1 + |m|) ^ |s|`.

```lean
TauCeti.CircleSobolev.weight_add_le (s : ℝ) (m n : ℤ) :
  TauCeti.CircleSobolev.weight s (m + n) ≤
    TauCeti.CircleSobolev.weight |s| m * TauCeti.CircleSobolev.weight s n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.weight_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.weight_add_le).

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.weight_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.weight_add_le)
- [Source of `TauCeti.CircleSobolev.weight_add_le` in TauCeti/Analysis/Sobolev/Circle/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Circle/Basic.lean#L139)
