// Обновленный JS
gsap.registerPlugin(ScrollTrigger);

gsap.utils.toArray('.parallax').forEach(layer => {
    const speed = parseFloat(layer.dataset.speed);
    const yPosition = -500 * speed;

    gsap.to(layer, {
        y: yPosition,
        ease: 'none',
        scrollTrigger: {
            trigger: layer,
            start: 'top top',
            end: 'bottom top',
            scrub: 0.5,
        },
    });
});

gsap.to(".layers", {
    y: -500,
    scrollTrigger: {
        trigger: ".layers",
        start: "top top",
        end: "bottom top",
        scrub: 1,
    },
});
