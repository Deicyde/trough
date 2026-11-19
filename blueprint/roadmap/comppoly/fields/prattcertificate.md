---
catalog: module
lean: Nat.Prime.dvd_mul_list, PrattPartList, PrattCertificate', PrattPartList.out, PrattCertificate'.out, PrattPart, PrattCertificate, PrattPart.out, PrattCertificate.out, prime_2, prime_3, prime_5, prime_7, prime_11, prime_13, prime_17, prime_19, prime_23, prime_29, prime_31, prime_37, prime_41, prime_43, prime_47, prime_101, powMod, PowTwoRepr, factorOutTwos, millerRabinBases, deterministicMillerRabin, g, rho', rho, factor, PrimeWithMultiplicity, factor', UnverifiedPrattPart, UnverifiedPrattCertificate, computePrattPart, computePrattCertificate, Tactic.verifySmallPrime, Tactic.ZMod.powEqOfPowMod, Tactic.ZMod.bla, Tactic.verifyEqOne, Tactic.ZMod.powNeOfPowMod, Tactic.ZMod.blub, Tactic.verifyNeOne, Tactic.verifyCertificate, Tactic.Nat.Prime_of_isNat
statement: formalized
proof: formalized
---

# The Lucas test for primes

`CompPoly.Fields.PrattCertificate`, in [CompPoly/Fields/PrattCertificate.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean), by Bolton Bailey.

> This file implements the Lucas test for primes (not to be confused with the Lucas-Lehmer test for
> Mersenne primes). A number `a` witnesses that `n` is prime if `a` has order `n-1` in the
> multiplicative group of integers mod `n`. This is checked by verifying that `a^(n-1) = 1 (mod n)`
> and `a^d ≠ 1 (mod n)` for any divisor `d | n - 1`. This test is the basis of the Pratt primality
> certificate.
>
> …
>
> ## Implementation notes
>
> Note that the proof for `lucas_primality` relies on analyzing the multiplicative group
> modulo `p`. Despite this, the theorem still holds vacuously for `p = 0` and `p = 1`: In these
> cases, we can take `q` to be any prime and see that `hd` does not hold, since `a^((p-1)/q)` reduces
> to `1`.

`Nat.Prime.dvd_mul_list` (lemma, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L40))

```lean
lemma Nat.Prime.dvd_mul_list {p : ℕ} {l : List ℕ} (h : p.Prime) :
    p ∣ l.prod ↔ ∃ r ∈ l, p ∣ r
```

`PrattPartList` (inductive type, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L66))

> Recursive form of a Pratt certificate for `p`, which may take in Pratt certificates
> for a list of prime powers `r` less than `p` whose product is equal to `p - 1`.

```lean
inductive PrattPartList : (p : ℕ) → (a : ZMod p) → ℕ → Prop
  | prime : {p : ℕ} → {a : ZMod p} → (n k nk : ℕ) → n.Prime →
      a ^ ((p - 1) / n) ≠ 1 → n ^ k = nk → PrattPartList p a nk
  | split : {p : ℕ} → {a : ZMod p} → {n : ℕ} → (list : List ℕ) →
      (∀ r ∈ list, PrattPartList p a r) → list.prod = n → PrattPartList p a n
```

`PrattCertificate'` (structure, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L74))

> Alternative form of a Pratt certificate for `p`, which may take in Pratt certificates
> for a list of prime powers `r` less than `p` whose product is equal to `p - 1`.

```lean
structure PrattCertificate' (p : ℕ) : Type where
  a : ZMod p
  pow_eq_one : a ^ (p - 1) = 1
  part : PrattPartList p a (p - 1)
```

`PrattPartList.out` (theorem, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L79))

```lean
theorem PrattPartList.out {p : ℕ} {a : ZMod p} {n : ℕ} (h : PrattPartList p a n) :
    ∀ q : ℕ, q.Prime → q ∣ n → a ^ ((p - 1) / q) ≠ 1
```

`PrattCertificate'.out` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L93))

```lean
theorem PrattCertificate'.out {p : ℕ} (c : PrattCertificate' p) : p.Prime
```

`PrattPart` (inductive type, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L99))

> The binary version of `PrattPartList`. This is the one in the original file.

```lean
inductive PrattPart : (p : ℕ) → (a : ZMod p) → ℕ → Prop
  | prime : {p : ℕ} → {a : ZMod p} → (n k nk : ℕ) → n.Prime →
      a ^ ((p - 1) / n) ≠ 1 → n ^ k = nk → PrattPart p a nk
  | split : {p : ℕ} → {a : ZMod p} → {n : ℕ} → (l r : ℕ) →
      PrattPart p a l → PrattPart p a r → l * r = n → PrattPart p a n
```

`PrattCertificate` (structure, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L105))

```lean
structure PrattCertificate (p : ℕ) : Type where
  a : ZMod p
  pow_eq_one : a ^ (p - 1) = 1
  part : PrattPart p a (p - 1)
```

`PrattPart.out` (theorem, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L110))

```lean
theorem PrattPart.out {p : ℕ} {a : ZMod p} {n : ℕ} (h : PrattPart p a n) :
    ∀ q : ℕ, q.Prime → q ∣ n → a ^ ((p - 1) / q) ≠ 1
```

`PrattCertificate.out` (theorem, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L125))

```lean
theorem PrattCertificate.out {p : ℕ} (c : PrattCertificate p) : p.Prime
```

`prime_2` (theorem, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L130))

```lean
theorem prime_2 : Nat.Prime 2
```

`prime_3` (theorem, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L131))

```lean
theorem prime_3 : Nat.Prime 3
```

`prime_5` (theorem, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L132))

```lean
theorem prime_5 : Nat.Prime 5
```

`prime_7` (theorem, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L135))

```lean
theorem prime_7 : Nat.Prime 7
```

`prime_11` (theorem, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L140))

```lean
theorem prime_11 : Nat.Prime 11
```

`prime_13` (theorem, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L145))

```lean
theorem prime_13 : Nat.Prime 13
```

`prime_17` (theorem, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L150))

```lean
theorem prime_17 : Nat.Prime 17
```

`prime_19` (theorem, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L153))

```lean
theorem prime_19 : Nat.Prime 19
```

`prime_23` (theorem, [line 158](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L158))

```lean
theorem prime_23 : Nat.Prime 23
```

`prime_29` (theorem, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L163))

```lean
theorem prime_29 : Nat.Prime 29
```

`prime_31` (theorem, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L168))

```lean
theorem prime_31 : Nat.Prime 31
```

`prime_37` (theorem, [line 175](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L175))

```lean
theorem prime_37 : Nat.Prime 37
```

`prime_41` (theorem, [line 180](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L180))

```lean
theorem prime_41 : Nat.Prime 41
```

`prime_43` (theorem, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L185))

```lean
theorem prime_43 : Nat.Prime 43
```

`prime_47` (theorem, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L192))

```lean
theorem prime_47 : Nat.Prime 47
```

`prime_101` (theorem, [line 198](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L198))

```lean
theorem prime_101 : Nat.Prime 101
```

`powMod` (definition, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L210))

```lean
meta def powMod (a b m : ℕ) : ℕ
```

`PowTwoRepr` (structure, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L223))

```lean
structure PowTwoRepr where
  two_exp : ℕ
  odd_part : ℕ
```

`factorOutTwos` (definition, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L227))

```lean
meta def factorOutTwos (n : ℕ) : PowTwoRepr
```

`millerRabinBases` (definition, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L237))

```lean
meta def millerRabinBases : List ℕ
```

`deterministicMillerRabin` (definition, [line 240](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L240))

```lean
meta def deterministicMillerRabin (n : ℕ) : Bool
```

`g` (definition, [line 262](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L262))

```lean
meta def g (n : ℕ) (c : ℕ) (x : ℕ)
```

`rho'` (definition, [line 265](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L265))

> Auxiliary function for `rho` that tries to find a factor of `n`

```lean
meta def rho' (n : ℕ) (start : ℕ) (c : ℕ) : Option ℕ
```

`rho` (definition, [line 283](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L283))

```lean
meta def rho (n : ℕ) : Option ℕ
```

`factor` (definition, [line 291](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L291))

```lean
meta partial def factor (n : ℕ) : Option (List ℕ)
```

`PrimeWithMultiplicity` (structure, [line 300](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L300))

```lean
structure PrimeWithMultiplicity : Type where
  prime : ℕ
  multiplicity : ℕ
deriving Repr
```

`factor'` (definition, [line 306](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L306))

> Factor `n` into a list of prime numbers with their multiplicities

```lean
meta def factor' (n : ℕ) : Option (List PrimeWithMultiplicity)
```

`UnverifiedPrattPart` (inductive type, [line 313](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L313))

```lean
inductive UnverifiedPrattPart : Type
  | prime : (p : ℕ) → (k : ℕ) → (hp : UnverifiedPrattCertificate p) → UnverifiedPrattPart
  | split : UnverifiedPrattPart → UnverifiedPrattPart → UnverifiedPrattPart
deriving Repr
```

`UnverifiedPrattCertificate` (inductive type, [line 318](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L318))

```lean
inductive UnverifiedPrattCertificate : ℕ → Type
  | knownPrime : (n : ℕ) → UnverifiedPrattCertificate n
  | of : (n : ℕ) → (a : ℕ) → (part : UnverifiedPrattPart) → UnverifiedPrattCertificate n
deriving Repr
```

`computePrattPart` (definition, [line 331](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L331))

```lean
meta partial def computePrattPart (l : List PrimeWithMultiplicity) :
    Option UnverifiedPrattPart
```

`computePrattCertificate` (definition, [line 342](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L342))

```lean
meta partial def computePrattCertificate (n : ℕ) : Option (UnverifiedPrattCertificate n)
```

`Tactic.verifySmallPrime` (definition, [line 375](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L375))

```lean
meta def verifySmallPrime (n' : Q(ℕ)) : MetaM Q(Nat.Prime $n')
```

`Tactic.ZMod.powEqOfPowMod` (theorem, [line 394](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L394))

```lean
theorem ZMod.powEqOfPowMod :
    ∀ {n a' c : ℕ} (a : ZMod n), (a' : ZMod n) = a →
      Nat.mod (Nat.pow a' (n - 1)) n = c → c = 1 → a ^ (n - 1) = 1
```

`Tactic.ZMod.bla` (theorem, [line 401](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L401))

```lean
theorem ZMod.bla : ∀ {n c : ℕ} (a : ZMod n), c = 1 → IsNat (a ^ (n - 1)) c → a ^ (n - 1) = 1
```

`Tactic.verifyEqOne` (definition, [line 406](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L406))

```lean
meta def verifyEqOne (n a' : Q(ℕ)) (a : Q(ZMod $n)) (_ : Q(($a' : ZMod $n) = $a)) :
    MetaM Q($a ^ ($n - 1) = 1)
```

`Tactic.ZMod.powNeOfPowMod` (theorem, [line 427](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L427))

```lean
theorem ZMod.powNeOfPowMod :
    ∀ {n a' q c : ℕ} (a : ZMod n), (a' : ZMod n) = a → decide (n ≥ 2) = true →
      Nat.mod (Nat.pow a' ((n - 1) / q)) n = c → decide (c ≠ 1) = true → a ^ ((n - 1) / q) ≠ 1
  | n, a, q, _, _, rfl, hn, rfl, h => by
    rw [← Nat.cast_pow]
    conv_rhs => rw [← Nat.cast_one]
    intro h'
    rw [CharP.natCast_eq_natCast (ZMod n) n] at h'
    replace h
```

`Tactic.ZMod.blub` (theorem, [line 444](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L444))

```lean
theorem ZMod.blub :
    ∀ {n q c : ℕ} (a : ZMod n), (decide (n ≥ 2) = true) → (decide (c < n) = true) →
      (decide (c ≠ 1) = true) → IsNat (a ^ ((n - 1) / q)) c → a ^ ((n - 1) / q) ≠ 1
```

`Tactic.verifyNeOne` (definition, [line 456](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L456))

```lean
meta def verifyNeOne (n a' q : Q(ℕ)) (a : Q(ZMod $n)) (_ : Q(($a' : ZMod $n) = $a)) :
    MetaM Q($a ^ (($n - 1) / $q) ≠ 1)
```

`Tactic.verifyCertificate` (definition, [line 473](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L473))

```lean
meta partial def verifyCertificate (n' : Q(ℕ)) (n : ℕ) :
    UnverifiedPrattCertificate n → MetaM Q(Nat.Prime $n')
  | .knownPrime n => verifySmallPrime n'
  | .of n a part => do
      let cert ← generateCertificate n' n a part
      return q(PrattCertificate.out $cert)
```

`Tactic.Nat.Prime_of_isNat` (theorem, [line 507](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean#L507))

```lean
theorem Nat.Prime_of_isNat : ∀ {n n' : ℕ}, IsNat n n' → n'.Prime → n.Prime
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/PrattCertificate.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/PrattCertificate.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Fields.PrattCertificate.json)
