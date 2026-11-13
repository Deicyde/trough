---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.FisherKPP.IsWaveProfile, MathlibExt.Biology.Dynamics.FisherKPP.IsFront, MathlibExt.Biology.Dynamics.FisherKPP.hasDerivAt_wave_t, MathlibExt.Biology.Dynamics.FisherKPP.hasDerivAt_wave_x, MathlibExt.Biology.Dynamics.FisherKPP.hasDerivAt_wave_xx, MathlibExt.Biology.Dynamics.FisherKPP.not_eventually_pos_of_sq_lt, MathlibExt.Biology.Dynamics.FisherKPP.not_isFront_of_sq_lt, MathlibExt.Biology.Dynamics.FisherKPP.azRate
statement: formalized
proof: formalized
---

# Fisher–KPP travelling waves

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html).

## Traveling-wave profile of the Fisher–KPP equation

`U` is a traveling-wave profile of speed `c` for `∂u/∂t = D ∂²u/∂x² + r u (1 - u)`: it is
twice differentiable with first derivative `U'` and `U'' = -(c U' + r U (1 - U)) / D`, which for
`D ≠ 0` is the profile equation `D U'' + c U' + r U (1 - U) = 0`.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.IsWaveProfile`, a definition declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#is-wave-profile).

## Traveling front of the Fisher–KPP equation

A traveling front of speed `c`: a wave profile with `0 < U < 1`, `U → 1` at `-∞` and
`U → 0` at `+∞`.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.IsFront`, a definition declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#is-front).

## Time derivative of a traveling wave

Time derivative of the wave `u(x, t) = U(x - c t)`: `∂u/∂t = -c U'(x - c t)`.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.hasDerivAt_wave_t`, a theorem declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#has-deriv-at-wave-t).

## Space derivative of a traveling wave

Space derivative of the wave: `∂u/∂x = U'(x - c t)`.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.hasDerivAt_wave_x`, a theorem declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#has-deriv-at-wave-x).

## Traveling wave solves the Fisher–KPP equation

Second space derivative of the wave; with `hD : D ≠ 0` it gives the PDE
`-c U' = D U'' + r U (1 - U)`, i.e. `∂u/∂t = D ∂²u/∂x² + r u (1 - u)`.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.hasDerivAt_wave_xx`, a theorem declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#has-deriv-at-wave-xx).

## No traveling wave with `c² < 4 r D`

If `D, r > 0` and `c² < 4 r D`, a wave profile
tending to `0` at `+∞` is not eventually positive. (This excludes `|c| < 2 √(r D)`, not
`c < 2 √(r D)` for negative `c`.)

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.not_eventually_pos_of_sq_lt`, a theorem declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#not-eventually-pos-of-sq-lt).

## Minimal speed of Fisher–KPP traveling fronts

A front of speed `c` needs `c² ≥ 4 r D`; for `c ≥ 0` this is `c ≥ 2 √(r D)`.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.not_isFront_of_sq_lt`, a theorem declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#not-is-front-of-sq-lt).

## Rate of the Ablowitz–Zeppetella wave

The rate `κ = √(r / (6 D))` of the Ablowitz–Zeppetella wave.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.azRate`, a definition declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#az-rate).

## Speed of the Ablowitz–Zeppetella wave

The Ablowitz–Zeppetella speed `c = 5 √(r D / 6)` (`5 / √6` when `D = r = 1`).

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.azSpeed`, a definition declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#az-speed).

## Ablowitz–Zeppetella wave profile

The Ablowitz–Zeppetella profile `U(z) = (1 + C exp (κ z))⁻²`.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.azWave`, a definition declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#az-wave).

## Derivative of the Ablowitz–Zeppetella profile

The derivative of the Ablowitz–Zeppetella profile, `-2 κ C e^{κ z} (1 + C e^{κ z})⁻³`.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.azWaveDeriv`, a definition declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#az-wave-deriv).

## The Ablowitz–Zeppetella front

For `D, r, C > 0`, `(1 + C exp (z √(r / (6 D))))⁻²` is a
front of speed `5 √(r D / 6)`.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.isFront_azWave`, a theorem declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#is-front-az-wave).

## Ablowitz–Zeppetella speed exceeds the minimal front speed

The Ablowitz–Zeppetella speed exceeds the minimal speed: `2 √(r D) < 5 √(r D / 6)`.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.two_mul_sqrt_lt_azSpeed`, a theorem declared in [MathlibExt/Biology/Dynamics/FisherKPP.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPP.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#two-mul-sqrt-lt-az-speed).

## Kolmogorov–Petrovsky–Piskunov: fronts exist at every speed `c ≥ 2 √(r D)`

**Kolmogorov–Petrovsky–Piskunov: fronts exist at every speed `c ≥ 2 √(r D)`**, and they are
strictly decreasing.

Formalized by `MathlibExt.Biology.Dynamics.FisherKPP.exists_isFront_of_le`, a theorem declared in [MathlibExt/Biology/Dynamics/FisherKPPExistence.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FisherKPPExistence.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html#exists-is-front-of-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fisher–KPP travelling waves](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/pattern-formation/fisher-kpp-travelling-waves)
