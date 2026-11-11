---
declaration: section
origin: cited
lean: MathlibExt.Probability.CharFunTaylorBounds.norm_exp_ofReal_mul_I_sub_one_sub_le, MathlibExt.Probability.CharFunTaylorBounds.norm_charFun_sub_one_sub_le, MathlibExt.Probability.CharFunTaylorBounds.norm_charFun_sub_one_le, MathlibExt.Probability.CharFunTaylorBounds.norm_charFun_sub_one_le_sq_mul_variance
statement: formalized
proof: formalized
---

# Taylor bounds for characteristic functions

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/taylor-bounds-for-characteristic-functions/index.html).

## Global second-order bound for the imaginary exponential

For every real number $u$,
$|e^{iu} - 1 - iu| \le u^2$, with no restriction on the size of $u$.

The proof splits at $u^2 \le 27$: in that range the squared norm is
$(1 - \cos u)^2 + (u - \sin u)^2 \le u^4/4 + u^6/36 \le u^4$, using $1 - \cos u \le u^2/2$ and
$|u - \sin u| \le |u|^3/6$; outside that range $|u| > 5$ and the triangle inequality gives
$2 + |u| \le u^2$.

Formalized by `MathlibExt.Probability.CharFunTaylorBounds.norm_exp_ofReal_mul_I_sub_one_sub_le`, a theorem declared in [MathlibExt/Probability/CharFunTaylorBounds.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CharFunTaylorBounds.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/taylor-bounds-for-characteristic-functions/index.html#norm-exp-of-real-mul-i-sub-one-sub-le).

## Second-order Taylor bound for the characteristic function

Let $X$ be a measurable real
random variable on a probability space with $X^2$ integrable, and let $\varphi_X$ be the
characteristic function of the law of $X$. Then for every real $t$,
$|\varphi_X(t) - 1 - it\,\mathbb{E}[X]| \le t^2 \, \mathbb{E}[X^2]$.

Formalized by `MathlibExt.Probability.CharFunTaylorBounds.norm_charFun_sub_one_sub_le`, a theorem declared in [MathlibExt/Probability/CharFunTaylorBounds.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CharFunTaylorBounds.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/taylor-bounds-for-characteristic-functions/index.html#norm-char-fun-sub-one-sub-le).

## First-order Taylor bound for the characteristic function

Let $X$ be a measurable real
random variable on a probability space with $|X|$ integrable, and let $\varphi_X$ be the
characteristic function of the law of $X$. Then for every real $t$,
$|\varphi_X(t) - 1| \le |t| \, \mathbb{E}|X|$.

Formalized by `MathlibExt.Probability.CharFunTaylorBounds.norm_charFun_sub_one_le`, a theorem declared in [MathlibExt/Probability/CharFunTaylorBounds.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CharFunTaylorBounds.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/taylor-bounds-for-characteristic-functions/index.html#norm-char-fun-sub-one-le).

## Characteristic-function second-order bound

Let $X$ be a measurable real random variable
on a probability space with $\mathbb{E}[X] = 0$ and $X^2$ integrable, and let $\varphi_X$ be the
characteristic function of the law of $X$. Then for every real $t$,
$|\varphi_X(t) - 1| \le t^2 \, \mathbb{E}[X^2]$.

Formalized by `MathlibExt.Probability.CharFunTaylorBounds.norm_charFun_sub_one_le_sq_mul_variance`, a theorem declared in [MathlibExt/Probability/CharFunTaylorBounds.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CharFunTaylorBounds.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/taylor-bounds-for-characteristic-functions/index.html#norm-char-fun-sub-one-le-sq-mul-variance).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Taylor bounds for characteristic functions](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/taylor-bounds-for-characteristic-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/characteristic-functions/taylor-bounds-for-characteristic-functions)
