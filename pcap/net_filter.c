#include <sys/time.h>
#include <netinet/in.h>
#include <net/ethernet.h>
#include <pcap/pcap.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <netinet/udp.h>
#include <netinet/ip_icmp.h>
#include <arpa/inet.h>

#define PROMISCUOUS 	1
#define NONPROMISCUOUS	0

int id = 0;
struct ip *iph;
struct tcphdr *tcph;

void callback(u_char *useless, const struct pcap_pkthdr *pkthdr,
		const u_char *packet) {
	FILE *fp;
	static int count = 1;
	struct ether_header *ep;
	unsigned short ether_type;
	int chcnt = 0;
	int length = pkthdr->len;
	char buf[2048];

	ep = (struct ether_header *)packet;
	packet += sizeof(struct ether_header);
	ether_type = ntohs(ep->ether_type);
	memset(buf, 0, 2048);
	if (ether_type == ETHERTYPE_IP) {
		iph = (struct ip *)packet;
		// printf("Src Address	: %s\n", inet_ntoa(iph->ip_src));
		// printf("Dst Address	: %s\n", inet_ntoa(iph->ip_dst));
		// printf("----------------------------------------\n");
		if (iph->ip_p == IPPROTO_TCP) {
			tcph = (struct tcp *)(packet + iph->ip_hl * 4);
			printf("[*] TCP Packet Catched ..\n");
			id++;
			sprintf(buf, "./%d.%s", id, "packet");
			fp = fopen(buf, "wb");
			fwrite(packet, 1, sizeof(packet)+1, fp);
			fclose(fp);
			// printf("Src Port	: %d\n", ntohs(tcph->source));
			// printf("Dst Port	: %d\n", ntohs(tcph->dest));
		}
	}
}

int main(int argc, char **argv) {
	char *dev, *net, *mask;
	bpf_u_int32 netp, maskp;
	char errbuf[PCAP_ERRBUF_SIZE];
	int ret;
	struct pcap_pkthdr hdr;
	struct in_addr net_addr, mask_addr;
	struct ether_header *eptr;
	const u_char *packet;

	struct bpf_program fp;
	pcap_t *pcd;

	dev = pcap_lookupdev(errbuf);
	if (dev == NULL) {
		printf("[*] Error : %s\n", errbuf);
		exit(1);
	}
	printf("[*] Device : %s\n", dev);
	ret = pcap_lookupnet(dev, &netp, &maskp, errbuf);
	if (ret == -1) {
		printf("[*] Error : %s\n", errbuf);
		exit(1);
	}
	pcd = pcap_open_live(dev, BUFSIZ, NONPROMISCUOUS, -1, errbuf);
	if (pcd == NULL) {
		printf("[*] Error : %s\n", errbuf);
		exit(1);
	}
	printf("pcap_compile\n");
	if (pcap_compile(pcd, &fp, argv[2], 0, netp) == -1) {
		printf("compile error\n");
		exit(1);
	}
	printf("pcap_setfilter\n");
	if (pcap_setfilter(pcd, &fp) == -1) {
		printf("setfilter error\n");
		exit(0);
	}
	printf("pcap_loop\n");
	pcap_loop(pcd, atoi(argv[1]), callback, NULL);
}