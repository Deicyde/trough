# Austin laws

The singleton or empty magma satisfies all equational laws. It is natural to ask whether an equational law admits nontrivial finite or infinite models. If no model exists, then the law is equivalent to [E2](https://teorth.github.io/equational_theories/implications/?2) $({x = y})$. An *Austin law* is a law which admits infinite models, but no nontrivial finite models: the law is equivalent to [E2](https://teorth.github.io/equational_theories/implications/?2) for finite magmas. Austin \[[Austin 1965](https://doi.org/10.2307/2034688)\] established the first such law, namely the order $9$ law

$$
(((1 \diamond 1) \diamond 1) \diamond 0) \diamond (((1 \diamond 1) \diamond ((1 \diamond 1) \diamond 1)) \diamond 2) \simeq 0.
$$

A shorter Austin law of order $6$ was established in \[Kisielewicz 1990\]:

- [Kisielewicz's first Austin law](kis-thm.md)

An even shorter law (order $5$) was obtained by the same author in a follow-up paper \[[Kisielewicz 1997](https://doi.org/10.1007/s000120050057)\]:

- [Kisielewicz's second Austin law](kis-thm2.md)

In that paper a computer search was also used to show that no law of order four or less is an Austin law.

An open question is whether [E5093](https://teorth.github.io/equational_theories/implications/?5093) $({x = y \diamond (y \diamond (y \diamond (x \diamond (z \diamond y))))})$ is an Austin law. We have the following partial result from \[[Kisielewicz 1997](https://doi.org/10.1007/s000120050057)\]:

- [Equation 5093 has no non-trivial finite models](5093-nontrivial.md)

The following result was established in \[[Austin 1966](https://doi.org/10.2307/2035753)\]:

- [Austin's finite model theorem](austin-two.md)
