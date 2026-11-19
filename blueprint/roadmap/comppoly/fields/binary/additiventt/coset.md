---
catalog: module
lean: AdditiveNTT.Coset.point, AdditiveNTT.Coset.vanishing, AdditiveNTT.Coset.normalized, AdditiveNTT.Coset.novel, AdditiveNTT.Coset.novelEval, AdditiveNTT.Coset.ntt, AdditiveNTT.Coset.Independent, AdditiveNTT.Coset.IsCantor, AdditiveNTT.Coset.butterfly, AdditiveNTT.Coset.ibutterfly, AdditiveNTT.Coset.stage, AdditiveNTT.Coset.istage, AdditiveNTT.Coset.network, AdditiveNTT.Coset.inetwork, AdditiveNTT.Coset.twiddle, AdditiveNTT.Coset.sqAddIter, AdditiveNTT.Coset.point_eq_sum, AdditiveNTT.Coset.point_zero, AdditiveNTT.Coset.point_two_pow, AdditiveNTT.Coset.point_add_mul, AdditiveNTT.Coset.point_add_two_pow, AdditiveNTT.Coset.point_mul_two_pow, AdditiveNTT.Coset.point_congr, AdditiveNTT.Coset.map_point, AdditiveNTT.Coset.point_two_pow_sub_one, AdditiveNTT.Coset.vanishing_zero, AdditiveNTT.Coset.vanishing_succ, AdditiveNTT.Coset.vanishing_point, AdditiveNTT.Coset.vanishing_basis_ne_zero, AdditiveNTT.Coset.vanishing_add, AdditiveNTT.Coset.vanishingHom, AdditiveNTT.Coset.vanishing_succ', AdditiveNTT.Coset.normalized_add, AdditiveNTT.Coset.normalized_basis, AdditiveNTT.Coset.normalized_point, AdditiveNTT.Coset.normalized_shift_low, AdditiveNTT.Coset.normalized_shift_high, AdditiveNTT.Coset.novel_succ_low, AdditiveNTT.Coset.novel_succ_high, AdditiveNTT.Coset.sqAddIter_succ, AdditiveNTT.Coset.sqAddIter_basis, AdditiveNTT.Coset.vanishing_eq_sqAddIter, AdditiveNTT.Coset.vanishing_basis_cantor, AdditiveNTT.Coset.IsCantor.independent, AdditiveNTT.Coset.normalized_eq_sqAddIter, AdditiveNTT.Coset.twiddle_cantor, AdditiveNTT.Coset.stage_offset, AdditiveNTT.Coset.istage_offset, AdditiveNTT.Coset.stage_congr, AdditiveNTT.Coset.istage_congr, AdditiveNTT.Coset.istage_stage, AdditiveNTT.Coset.stage_istage, AdditiveNTT.Coset.inetwork_network, AdditiveNTT.Coset.network_inetwork, AdditiveNTT.Coset.network_twiddle_congr, AdditiveNTT.Coset.blocks_succ, AdditiveNTT.Coset.network_congr, AdditiveNTT.Coset.inetwork_congr, AdditiveNTT.Coset.network_offset, AdditiveNTT.Coset.inetwork_twiddle_congr, AdditiveNTT.Coset.inetwork_offset, AdditiveNTT.Coset.stage_top_low, AdditiveNTT.Coset.stage_top_high, AdditiveNTT.Coset.novelEval_congr, AdditiveNTT.Coset.novelEval_succ, AdditiveNTT.Coset.novelEval_add_smul, AdditiveNTT.Coset.twiddle_upper, AdditiveNTT.Coset.network_ntt, AdditiveNTT.Coset.inetwork_ntt, AdditiveNTT.Coset.novelEval_pad, AdditiveNTT.Coset.ntt_pad
statement: formalized
proof: formalized
---

# The additive NTT over a coset, and its inverse

`CompPoly.Fields.Binary.AdditiveNTT.Coset`, in [CompPoly/Fields/Binary/AdditiveNTT/Coset.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean), by Thomas Coratger.

> The transform of Lin, Chung and Han (FOCS 2014), over any coset shift + S_l.
>
> The other files here follow Diamond and Posen: one transform over S_l, tiled for the rate.
>
> `CosetBridge.lean` shows these objects agree with those of the other files.
>
> ## Main results
>
> - `vanishing_add`: W_i is additive in characteristic 2 (Lemma 1).
> - `network_ntt`: the butterfly network evaluates the novel-basis polynomial on the coset.
> - `inetwork_network`: the inverse network undoes the network.
> - `inetwork_ntt`: the inverse network recovers the coefficients.
> - `ntt_pad`: zero-padded coefficients split into one transform per coset of S_m.
> - `normalized_eq_sqAddIter`: for a Cantor basis, W^_j is the j-th iterate of x^2 + x.

`AdditiveNTT.Coset.point` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L46))

> Point m of the span of the basis: the sum of beta_r over the set bits r of m.

```lean
def point (β : ℕ → F) (m : ℕ) : F
```

`AdditiveNTT.Coset.vanishing` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L49))

> The subspace polynomial W_i: the product of x - s over the 2^i points s of S_i.

```lean
def vanishing (β : ℕ → F) (i : ℕ) (x : F) : F
```

`AdditiveNTT.Coset.normalized` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L52))

> The normalised subspace polynomial W_i(x) / W_i(beta_i).

```lean
def normalized (β : ℕ → F) (i : ℕ) (x : F) : F
```

`AdditiveNTT.Coset.novel` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L55))

> The novel basis polynomial X_k of the first l normalised subspace polynomials.

```lean
def novel (β : ℕ → F) (l k : ℕ) (x : F) : F
```

`AdditiveNTT.Coset.novelEval` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L59))

> The value at x of sum_(k < 2^l) d_k X_k.

```lean
def novelEval (β : ℕ → F) (l : ℕ) (d : ℕ → V) (x : F) : V
```

`AdditiveNTT.Coset.ntt` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L63))

> The additive NTT over shift + S_l: entry i is sum_k d_k X_k at shift + point(i).

```lean
def ntt (β : ℕ → F) (l : ℕ) (shift : F) (d : ℕ → V) : ℕ → V
```

`AdditiveNTT.Coset.Independent` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L67))

> No beta_i, for i < n, is a point of the span of the earlier ones.

```lean
def Independent (β : ℕ → F) (n : ℕ) : Prop
```

`AdditiveNTT.Coset.IsCantor` (definition, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L70))

> A Cantor basis of length n: beta_0 = 1 and beta_i^2 + beta_i = beta_(i-1) for 0 < i < n.

```lean
def IsCantor (β : ℕ → F) (n : ℕ) : Prop
```

> ## The butterfly network

`AdditiveNTT.Coset.butterfly` (definition, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L76))

> The forward butterfly (u, v) -> (u + t v, u + t v + v).

```lean
def butterfly (t : F) (u v : V) : V × V
```

`AdditiveNTT.Coset.ibutterfly` (definition, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L79))

> The inverse butterfly (u, v) -> (u + t (u + v), u + v).

```lean
def ibutterfly (t : F) (u v : V) : V × V
```

`AdditiveNTT.Coset.stage` (definition, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L86))

> Stage j of the forward network.
>
> Row i pairs with the row 2^j away, inside its block of 2^(j+1) rows.
>
> Block b uses the twiddle tau(b).

```lean
def stage (τ : ℕ → F) (j : ℕ) (x : ℕ → V) : ℕ → V
```

`AdditiveNTT.Coset.istage` (definition, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L91))

> Stage j of the inverse network, pairing rows as the forward stage does.

```lean
def istage (τ : ℕ → F) (j : ℕ) (x : ℕ → V) : ℕ → V
```

`AdditiveNTT.Coset.network` (definition, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L96))

> The forward network of l stages, stage l - 1 first, stage j with twiddles tau_j.

```lean
def network (τ : ℕ → ℕ → F) : ℕ → (ℕ → V) → ℕ → V
```

`AdditiveNTT.Coset.inetwork` (definition, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L101))

> The inverse network of l stages: stage 0 first, up to stage l - 1.

```lean
def inetwork (τ : ℕ → ℕ → F) : ℕ → (ℕ → V) → ℕ → V
```

`AdditiveNTT.Coset.twiddle` (definition, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L106))

> The twiddle of stage j and block b over shift + S: W^_j at the block's first point.

```lean
def twiddle (β : ℕ → F) (shift : F) (j b : ℕ) : F
```

`AdditiveNTT.Coset.sqAddIter` (definition, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L110))

> The iterated map x -> x^2 + x, which is W_j for a Cantor basis.

```lean
def sqAddIter (j : ℕ) (x : F) : F
```

> ## Points

`AdditiveNTT.Coset.point_eq_sum` (theorem, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L124))

> Point m as a sum over any range of bits that covers m.

```lean
theorem point_eq_sum (β : ℕ → F) {m n : ℕ} (hm : m < 2 ^ n) :
    point β m = ∑ r ∈ range n, if m.testBit r then β r else 0
```

`AdditiveNTT.Coset.point_zero` (theorem, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L130))

```lean
theorem point_zero (β : ℕ → F) : point β 0 = 0
```

`AdditiveNTT.Coset.point_two_pow` (theorem, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L132))

```lean
theorem point_two_pow (β : ℕ → F) (j : ℕ) : point β (2 ^ j) = β j
```

`AdditiveNTT.Coset.point_add_mul` (theorem, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L138))

> Bits below 2^k and bits above it contribute separately.

```lean
theorem point_add_mul (β : ℕ → F) (a k : ℕ) {b : ℕ} (hb : b < 2 ^ k) :
    point β (2 ^ k * a + b) = point β (2 ^ k * a) + point β b
```

`AdditiveNTT.Coset.point_add_two_pow` (theorem, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L159))

```lean
theorem point_add_two_pow (β : ℕ → F) {m k : ℕ} (hm : m < 2 ^ k) :
    point β (m + 2 ^ k) = point β m + β k
```

`AdditiveNTT.Coset.point_mul_two_pow` (theorem, [line 164](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L164))

> Point m of a shifted basis is point m 2^s of the basis.

```lean
theorem point_mul_two_pow (β : ℕ → F) (m s : ℕ) :
    point β (2 ^ s * m) = point (fun r => β (s + r)) m
```

`AdditiveNTT.Coset.point_congr` (theorem, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L176))

> Point m only reads the basis vectors below the bit length of m.

```lean
theorem point_congr {β β' : ℕ → F} {m n : ℕ} (hm : m < 2 ^ n) (h : ∀ r < n, β r = β' r) :
    point β m = point β' m
```

`AdditiveNTT.Coset.map_point` (theorem, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L182))

> An additive map sends point m of a basis to point m of the image basis.

```lean
theorem map_point (f : F →+ F) (β : ℕ → F) (m : ℕ) : f (point β m) = point (f ∘ β) m
```

`AdditiveNTT.Coset.point_two_pow_sub_one` (theorem, [line 187](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L187))

> With every bit below t set, point (2^t - 1) is the sum of the first t basis vectors.

```lean
theorem point_two_pow_sub_one (β : ℕ → F) (t : ℕ) :
    point β (2 ^ t - 1) = ∑ q ∈ range t, β q
```

`AdditiveNTT.Coset.vanishing_zero` (theorem, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L200))

```lean
theorem vanishing_zero (x : F) : vanishing β 0 x = x
```

`AdditiveNTT.Coset.vanishing_succ` (theorem, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L202))

```lean
theorem vanishing_succ (i : ℕ) (x : F) :
    vanishing β (i + 1) x = vanishing β i x * vanishing β i (x - β i)
```

`AdditiveNTT.Coset.vanishing_point` (theorem, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L210))

```lean
theorem vanishing_point {i m : ℕ} (hm : m < 2 ^ i) : vanishing β i (point β m) = 0
```

`AdditiveNTT.Coset.vanishing_basis_ne_zero` (theorem, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L214))

> The scaling factor of the normalisation is nonzero for an independent basis.

```lean
theorem vanishing_basis_ne_zero {n i : ℕ} (hβ : Independent β n) (hi : i < n) :
    vanishing β i (β i) ≠ 0
```

`AdditiveNTT.Coset.vanishing_add` (theorem, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L223))

> Lin, Chung and Han, Lemma 1: W_i is additive in characteristic 2.

```lean
theorem vanishing_add (i : ℕ) (x y : F) :
    vanishing β i (x + y) = vanishing β i x + vanishing β i y
```

`AdditiveNTT.Coset.vanishingHom` (definition, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L234))

> W_i as an additive map.

```lean
def vanishingHom (i : ℕ) : F →+ F
```

`AdditiveNTT.Coset.vanishing_succ'` (theorem, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L242))

```lean
theorem vanishing_succ' (i : ℕ) (x : F) :
    vanishing β (i + 1) x = vanishing β i x * (vanishing β i x + vanishing β i (β i))
```

`AdditiveNTT.Coset.normalized_add` (theorem, [line 246](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L246))

```lean
theorem normalized_add (i : ℕ) (x y : F) :
    normalized β i (x + y) = normalized β i x + normalized β i y
```

`AdditiveNTT.Coset.normalized_basis` (theorem, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L251))

```lean
theorem normalized_basis {n i : ℕ} (hβ : Independent β n) (hi : i < n) :
    normalized β i (β i) = 1
```

`AdditiveNTT.Coset.normalized_point` (theorem, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L256))

```lean
theorem normalized_point {i m : ℕ} (hm : m < 2 ^ i) : normalized β i (point β m) = 0
```

`AdditiveNTT.Coset.normalized_shift_low` (theorem, [line 260](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L260))

> W^_l is constant on a coset of S_l.

```lean
theorem normalized_shift_low (l : ℕ) (shift : F) {i : ℕ} (hi : i < 2 ^ l) :
    normalized β l (shift + point β i) = normalized β l shift
```

`AdditiveNTT.Coset.normalized_shift_high` (theorem, [line 265](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L265))

> W^_l rises by one on the next coset of S_l.

```lean
theorem normalized_shift_high {n l : ℕ} (hβ : Independent β n) (hl : l < n) (shift : F)
    {i : ℕ} (hi : i < 2 ^ l) :
    normalized β l (shift + point β (i + 2 ^ l)) = normalized β l shift + 1
```

> ## The novel basis

`AdditiveNTT.Coset.novel_succ_low` (theorem, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L275))

```lean
theorem novel_succ_low (l : ℕ) {k : ℕ} (hk : k < 2 ^ l) (x : F) :
    novel β (l + 1) k x = novel β l k x
```

`AdditiveNTT.Coset.novel_succ_high` (theorem, [line 279](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L279))

```lean
theorem novel_succ_high (l : ℕ) {k : ℕ} (hk : k < 2 ^ l) (x : F) :
    novel β (l + 1) (k + 2 ^ l) x = novel β l k x * normalized β l x
```

> ## Cantor bases

`AdditiveNTT.Coset.sqAddIter_succ` (theorem, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L295))

```lean
theorem sqAddIter_succ (j : ℕ) (x : F) :
    sqAddIter (j + 1) x = sqAddIter j x ^ 2 + sqAddIter j x
```

`AdditiveNTT.Coset.sqAddIter_basis` (theorem, [line 301](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L301))

> The iterate sends beta_i to beta_(i-j).

```lean
theorem sqAddIter_basis {n : ℕ} (hβ : IsCantor β n) {i j : ℕ} (hi : i < n) (hj : j ≤ i) :
    sqAddIter j (β i) = β (i - j)
```

`AdditiveNTT.Coset.vanishing_eq_sqAddIter` (theorem, [line 311](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L311))

> For a Cantor basis, W_j is the j-th iterate of x^2 + x.

```lean
theorem vanishing_eq_sqAddIter {n : ℕ} (hβ : IsCantor β n) {j : ℕ} (hj : j ≤ n) (x : F) :
    vanishing β j x = sqAddIter j x
```

`AdditiveNTT.Coset.vanishing_basis_cantor` (theorem, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L320))

```lean
theorem vanishing_basis_cantor {n : ℕ} (hβ : IsCantor β n) {j : ℕ} (hj : j < n) :
    vanishing β j (β j) = 1
```

`AdditiveNTT.Coset.IsCantor.independent` (theorem, [line 325](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L325))

> A Cantor basis is independent.

```lean
theorem IsCantor.independent {n : ℕ} (hβ : IsCantor β n) : Independent β n
```

`AdditiveNTT.Coset.normalized_eq_sqAddIter` (theorem, [line 332](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L332))

> For a Cantor basis, W^_j = W_j: the normalisation divides by one.

```lean
theorem normalized_eq_sqAddIter {n : ℕ} (hβ : IsCantor β n) {j : ℕ} (hj : j < n) (x : F) :
    normalized β j x = sqAddIter j x
```

`AdditiveNTT.Coset.twiddle_cantor` (theorem, [line 337](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L337))

> For a Cantor basis, the twiddle is W_j(shift) plus point(2b).

```lean
theorem twiddle_cantor {n : ℕ} (hβ : IsCantor β n) (shift : F) {j b : ℕ} (hj : j < n)
    (hb : b * 2 ^ (j + 1) < 2 ^ n) :
    twiddle β shift j b = sqAddIter j shift + point β (2 * b)
```

> ## Row arithmetic of one stage

`AdditiveNTT.Coset.stage_offset` (theorem, [line 371](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L371))

```lean
theorem stage_offset (τ : ℕ → F) (j c : ℕ) (x : ℕ → V) (i : ℕ) :
    stage τ j x (i + c * 2 ^ (j + 1)) =
      stage (fun b => τ (b + c)) j (fun r => x (r + c * 2 ^ (j + 1))) i
```

`AdditiveNTT.Coset.istage_offset` (theorem, [line 384](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L384))

```lean
theorem istage_offset (τ : ℕ → F) (j c : ℕ) (x : ℕ → V) (i : ℕ) :
    istage τ j x (i + c * 2 ^ (j + 1)) =
      istage (fun b => τ (b + c)) j (fun r => x (r + c * 2 ^ (j + 1))) i
```

`AdditiveNTT.Coset.stage_congr` (theorem, [line 397](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L397))

```lean
theorem stage_congr {τ τ' : ℕ → F} {j c : ℕ} {x x' : ℕ → V} (hτ : ∀ b < c, τ b = τ' b)
    (hx : ∀ i < c * 2 ^ (j + 1), x i = x' i) {i : ℕ} (hi : i < c * 2 ^ (j + 1)) :
    stage τ j x i = stage τ' j x' i
```

`AdditiveNTT.Coset.istage_congr` (theorem, [line 406](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L406))

```lean
theorem istage_congr {τ τ' : ℕ → F} {j c : ℕ} {x x' : ℕ → V} (hτ : ∀ b < c, τ b = τ' b)
    (hx : ∀ i < c * 2 ^ (j + 1), x i = x' i) {i : ℕ} (hi : i < c * 2 ^ (j + 1)) :
    istage τ j x i = istage τ' j x' i
```

> ## The inverse network undoes the forward network

`AdditiveNTT.Coset.istage_stage` (theorem, [line 444](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L444))

```lean
theorem istage_stage (τ : ℕ → F) (j : ℕ) (x : ℕ → V) : istage τ j (stage τ j x) = x
```

`AdditiveNTT.Coset.stage_istage` (theorem, [line 459](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L459))

```lean
theorem stage_istage (τ : ℕ → F) (j : ℕ) (x : ℕ → V) : stage τ j (istage τ j x) = x
```

`AdditiveNTT.Coset.inetwork_network` (theorem, [line 475](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L475))

> The inverse network undoes the forward network, for any twiddles.

```lean
theorem inetwork_network (τ : ℕ → ℕ → F) (l : ℕ) (x : ℕ → V) :
    inetwork τ l (network τ l x) = x
```

`AdditiveNTT.Coset.network_inetwork` (theorem, [line 482](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L482))

> The forward network undoes the inverse network, for any twiddles.

```lean
theorem network_inetwork (τ : ℕ → ℕ → F) (l : ℕ) (x : ℕ → V) :
    network τ l (inetwork τ l x) = x
```

> ## Rows a network reads

`AdditiveNTT.Coset.network_twiddle_congr` (theorem, [line 495](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L495))

> The network only reads the twiddles of its l stages.

```lean
theorem network_twiddle_congr {τ τ' : ℕ → ℕ → F} {l : ℕ} (h : ∀ j < l, τ j = τ' j)
    (x : ℕ → V) : network τ l x = network τ' l x
```

`AdditiveNTT.Coset.blocks_succ` (theorem, [line 501](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L501))

```lean
theorem blocks_succ {c l j : ℕ} (hj : j < l) :
    c * 2 ^ (l + 1 - 1 - j) = 2 * c * 2 ^ (l - 1 - j)
```

`AdditiveNTT.Coset.network_congr` (theorem, [line 506](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L506))

> The rows of c whole blocks of 2^l depend only on those rows and their blocks' twiddles.

```lean
theorem network_congr {τ τ' : ℕ → ℕ → F} {l c : ℕ} {x x' : ℕ → V}
    (hτ : ∀ j < l, ∀ b < c * 2 ^ (l - 1 - j), τ j b = τ' j b)
    (hx : ∀ i < c * 2 ^ l, x i = x' i) {i : ℕ} (hi : i < c * 2 ^ l) :
    network τ l x i = network τ' l x' i
```

`AdditiveNTT.Coset.inetwork_congr` (theorem, [line 519](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L519))

```lean
theorem inetwork_congr {τ τ' : ℕ → ℕ → F} {l c : ℕ} {x x' : ℕ → V}
    (hτ : ∀ j < l, ∀ b < c * 2 ^ (l - 1 - j), τ j b = τ' j b)
    (hx : ∀ i < c * 2 ^ l, x i = x' i) {i : ℕ} (hi : i < c * 2 ^ l) :
    inetwork τ l x i = inetwork τ' l x' i
```

`AdditiveNTT.Coset.network_offset` (theorem, [line 535](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L535))

> Past c whole blocks of 2^l, the network is that of the rows above.
>
> The blocks are renumbered from zero.

```lean
theorem network_offset (τ : ℕ → ℕ → F) (l c : ℕ) (x : ℕ → V) (i : ℕ) :
    network τ l x (i + c * 2 ^ l) =
      network (fun j b => τ j (b + c * 2 ^ (l - 1 - j))) l (fun r => x (r + c * 2 ^ l)) i
```

`AdditiveNTT.Coset.inetwork_twiddle_congr` (theorem, [line 548](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L548))

```lean
theorem inetwork_twiddle_congr {τ τ' : ℕ → ℕ → F} {l : ℕ} (h : ∀ j < l, τ j = τ' j)
    (x : ℕ → V) : inetwork τ l x = inetwork τ' l x
```

`AdditiveNTT.Coset.inetwork_offset` (theorem, [line 557](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L557))

> Past c whole blocks of 2^l, the inverse network is that of the rows above.
>
> The blocks are renumbered from zero.

```lean
theorem inetwork_offset (τ : ℕ → ℕ → F) (l c : ℕ) (x : ℕ → V) (i : ℕ) :
    inetwork τ l x (i + c * 2 ^ l) =
      inetwork (fun j b => τ j (b + c * 2 ^ (l - 1 - j))) l (fun r => x (r + c * 2 ^ l)) i
```

> ## The top stage of a network of 2^(l+1) rows

`AdditiveNTT.Coset.stage_top_low` (theorem, [line 575](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L575))

```lean
theorem stage_top_low (τ : ℕ → F) (l : ℕ) (d : ℕ → V) {k : ℕ} (hk : k < 2 ^ l) :
    stage τ l d k = d k + τ 0 • d (k + 2 ^ l)
```

`AdditiveNTT.Coset.stage_top_high` (theorem, [line 580](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L580))

```lean
theorem stage_top_high (τ : ℕ → F) (l : ℕ) (d : ℕ → V) {k : ℕ} (hk : k < 2 ^ l) :
    stage τ l d (k + 2 ^ l) = d k + τ 0 • d (k + 2 ^ l) + d (k + 2 ^ l)
```

> ## Evaluations in the novel basis

`AdditiveNTT.Coset.novelEval_congr` (theorem, [line 587](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L587))

```lean
theorem novelEval_congr (β : ℕ → F) (l : ℕ) {d d' : ℕ → V} (h : ∀ k < 2 ^ l, d k = d' k)
    (x : F) : novelEval β l d x = novelEval β l d' x
```

`AdditiveNTT.Coset.novelEval_succ` (theorem, [line 592](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L592))

> Splitting the novel basis at bit l: sum_k d_k X_k = P_0 + W^_l P_1.

```lean
theorem novelEval_succ (β : ℕ → F) (l : ℕ) (d : ℕ → V) (x : F) :
    novelEval β (l + 1) d x =
      novelEval β l d x + normalized β l x • novelEval β l (fun k => d (k + 2 ^ l)) x
```

`AdditiveNTT.Coset.novelEval_add_smul` (theorem, [line 601](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L601))

```lean
theorem novelEval_add_smul (β : ℕ → F) (l : ℕ) (a b : ℕ → V) (t x : F) :
    novelEval β l (fun k => a k + t • b k) x = novelEval β l a x + t • novelEval β l b x
```

> ## The network computes the additive NTT

`AdditiveNTT.Coset.twiddle_upper` (theorem, [line 613](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L613))

> The twiddles of the upper half are those of the coset shifted by beta_l.

```lean
theorem twiddle_upper (β : ℕ → F) (shift : F) {l j b : ℕ} (hj : j < l)
    (hb : b < 2 ^ (l - 1 - j)) :
    twiddle β shift j (b + 1 * 2 ^ (l - 1 - j)) = twiddle β (shift + β l) j b
```

`AdditiveNTT.Coset.network_ntt` (theorem, [line 628](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L628))

> Lin, Chung and Han, section III: the network computes the additive NTT.
>
> The twiddles are W^_j at the block points, and the basis is independent.

```lean
theorem network_ntt (β : ℕ → F) {n l : ℕ} (hβ : Independent β n) (hl : l ≤ n) (shift : F)
    (d : ℕ → V) {i : ℕ} (hi : i < 2 ^ l) :
    network (twiddle β shift) l d i = ntt β l shift d i
```

`AdditiveNTT.Coset.inetwork_ntt` (theorem, [line 656](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L656))

> The inverse network recovers the coefficients from the values on the coset.

```lean
theorem inetwork_ntt (β : ℕ → F) {n l : ℕ} (hβ : Independent β n) (hl : l ≤ n) (shift : F)
    (d y : ℕ → V) (hy : ∀ i < 2 ^ l, y i = ntt β l shift d i) {i : ℕ} (hi : i < 2 ^ l) :
    inetwork (twiddle β shift) l y i = d i
```

`AdditiveNTT.Coset.novelEval_pad` (theorem, [line 665](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L665))

```lean
theorem novelEval_pad (β : ℕ → F) {m : ℕ} (d : ℕ → V) (hd : ∀ k, 2 ^ m ≤ k → d k = 0) (r : ℕ)
    (x : F) : novelEval β (m + r) d x = novelEval β m d x
```

`AdditiveNTT.Coset.ntt_pad` (theorem, [line 679](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean#L679))

> Coefficients zero from 2^m on: row c 2^m + i over S_(m+r) is row i over point(c 2^m) + S_m.

```lean
theorem ntt_pad (β : ℕ → F) {m : ℕ} (r : ℕ) (shift : F) (d : ℕ → V)
    (hd : ∀ k, 2 ^ m ≤ k → d k = 0) (c : ℕ) {i : ℕ} (hi : i < 2 ^ m) :
    ntt β (m + r) shift d (c * 2 ^ m + i) = ntt β m (shift + point β (c * 2 ^ m)) d i
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Binary/AdditiveNTT/Coset.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/Coset.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.AdditiveNTT.Coset.json)
