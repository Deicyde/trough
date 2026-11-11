---
declaration: theorem
origin: cited
lean: Polynomial.subresultant_eq_zero_of_getElem?_sturmSeq, Polynomial.exists_subresultant_natDegree_eq_C_mul_of_getElem?_sturmSeq, Polynomial.exists_subresultant_natDegree_sub_one_eq_C_mul_of_getElem?_sturmSeq
statement: formalized
proof: formalized
---

# Structure theorem for subresultants, degree gap

For consecutive entries `s, t` of the
signed remainder sequence of `p` and `q` after the first, the subresultants of `p` and `q` at
the indices strictly between `deg t` and `deg s - 1` vanish.

```lean
Polynomial.subresultant_eq_zero_of_getElem?_sturmSeq.{u_1} {K : Type u_1} [Field K] [DecidableEq K]
  {p q s t : Polynomial K} {m i j : ℕ} (hp : p.natDegree ≤ m) (hs : (p.sturmSeq q)[i + 1]? = some s)
  (ht : (p.sturmSeq q)[i + 2]? = some t) (htj : t.natDegree < j) (hjs : j + 1 < s.natDegree) :
  p.subresultant q m q.natDegree j = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.subresultant_eq_zero_of_getElem?_sturmSeq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Subresultant/Structure.html#Polynomial.subresultant_eq_zero_of_getElem?_sturmSeq).

## Other forms

**Structure theorem for subresultants, lower index.** Formalized in Tau Ceti as [`Polynomial.exists_subresultant_natDegree_eq_C_mul_of_getElem?_sturmSeq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Subresultant/Structure.html#Polynomial.exists_subresultant_natDegree_eq_C_mul_of_getElem?_sturmSeq).

```lean
Polynomial.exists_subresultant_natDegree_eq_C_mul_of_getElem?_sturmSeq.{u_1} {K : Type u_1}
  [Field K] [DecidableEq K] {p q s t : Polynomial K} {m i : ℕ} (hp : p.natDegree ≤ m)
  (hq : i = 0 → q.natDegree ≤ m) (hs : (p.sturmSeq q)[i + 1]? = some s)
  (ht : (p.sturmSeq q)[i + 2]? = some t) :
  ∃ c, c ≠ 0 ∧ p.subresultant q m q.natDegree t.natDegree = Polynomial.C c * t
```

**Structure theorem for subresultants, upper index.** Formalized in Tau Ceti as [`Polynomial.exists_subresultant_natDegree_sub_one_eq_C_mul_of_getElem?_sturmSeq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Subresultant/Structure.html#Polynomial.exists_subresultant_natDegree_sub_one_eq_C_mul_of_getElem?_sturmSeq).

```lean
Polynomial.exists_subresultant_natDegree_sub_one_eq_C_mul_of_getElem?_sturmSeq.{u_1} {K : Type u_1}
  [Field K] [DecidableEq K] {p q s t : Polynomial K} {m i : ℕ} (hp : p.natDegree ≤ m)
  (hq : i = 0 → q.natDegree ≤ m) (hs : (p.sturmSeq q)[i + 1]? = some s)
  (ht : (p.sturmSeq q)[i + 2]? = some t) :
  ∃ c, c ≠ 0 ∧ p.subresultant q m q.natDegree (s.natDegree - 1) = Polynomial.C c * t
```

## Sources

- [Tau Ceti documentation: `Polynomial.subresultant_eq_zero_of_getElem?_sturmSeq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Subresultant/Structure.html#Polynomial.subresultant_eq_zero_of_getElem?_sturmSeq)
- [Source of `Polynomial.subresultant_eq_zero_of_getElem?_sturmSeq` in TauCeti/RingTheory/Polynomial/Subresultant/Structure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Polynomial/Subresultant/Structure.lean#L109)
